import numpy as np


def dot_product(x, w1_w2, b):
    result = np.dot(x, w1_w2) + b

    result = result > 0
    # [[True, False, True, False]]

    result = result.astype(np.int32)
    # [[1, 0, 1, 0]]

    return result


def learning(x, y):
    # np.random.randint: [low, high) = low 이상, high 미만
    while True:
        w1_w2 = np.random.randint(-10, 11, (2, 1)) / 10
        b = np.random.randint(-10, 11, (1, 1)) / 10
        result = dot_product(x, w1_w2, b)

        if (result == y).all():
            return w1_w2, b


def xor(x, w1_w2):
    nand_result = dot_product(x, w1_w2['NAND']['w1_w2'], w1_w2['NAND']['bias'])
    or_result = dot_product(x, w1_w2['OR']['w1_w2'], w1_w2['OR']['bias'])

    x = np.concatenate((nand_result, or_result), axis=1)
    and_result = dot_product(x, w1_w2['AND']['w1_w2'], w1_w2['AND']['bias'])

    xor_result = and_result
    return xor_result


if __name__ == '__main__':
    dataset = np.array([[0, 0],
                        [1, 0],
                        [0, 1],
                        [1, 1]])

    # # 'AND', 'NAND', 'OR' 연산을 위한 가중치
    weight = {
        'AND': {},
        'NAND': {},
        'OR': {}
    }

    # AND 연산 학습
    and_output = np.array([[0],
                           [0],
                           [0],
                           [1]])
    weight['AND']['w1_w2'], weight['AND']['bias'] = learning(dataset, and_output)

    # NAND 연산 학습
    nand_output = np.array([[1],
                            [1],
                            [1],
                            [0]])
    weight['NAND']['w1_w2'], weight['NAND']['bias'] = learning(dataset, nand_output)

    # OR 연산 학습
    or_output = np.array([[0],
                          [1],
                          [1],
                          [1]])
    weight['OR']['w1_w2'], weight['OR']['bias'] = learning(dataset, or_output)

    print(f"weight = {weight}")
    # weight = {
    #     'AND': {
    #         'w1_w2': array([[0.9],
    #                         [0.4]]),
    #         'bias': array([[-1.]])
    #     },
    #     'NAND': {
    #         'w1_w2': array([[-0.6],
    #                         [-0.7]]),
    #         'bias': array([[1.]])
    #     },
    #     'OR': {
    #         'w1_w2': array([[0.9],
    #                         [1.]]),
    #         'bias': array([[-0.7]])
    #     }
    # }

    # XOR 연산
    xor_output = np.array([[0],
                           [1],
                           [1],
                           [0]])
    xor_result = xor(dataset, weight)

    print(f"xor_result: {xor_result}")
    print(f"result: {(xor_output == xor_result).all()}")
    # xor_result: [[0]
    #              [1]
    #              [1]
    #              [0]]
    # result: True
