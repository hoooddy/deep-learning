import numpy as np


def perceptron(x, w1_w2, b):
    result = np.dot(x, w1_w2) + b
    result = result > 0
    result = result.astype(np.int32)
    return result


def learning(x, y):
    # randint: [low, high) = low 이상, high 미만
    while True:
        w1_w2 = np.random.randint(-10, 11, (2, 1)) / 10
        b = np.random.randint(-10, 11, (1, 1)) / 10
        result = perceptron(x, w1_w2, b)

        if (result == y).all():
            return w1_w2, b


if __name__ == '__main__':
    dataset = np.array([[0, 0],
                        [1, 0],
                        [0, 1],
                        [1, 1]])

    # # 'AND', 'NAND', 'OR' 연산을 위한 가중치
    weight = {
        'AND': {},
        'NAND': {},
        'OR':  {}
    }

    # # AND 연산 학습
    and_output = np.array([[0],
                           [0],
                           [0],
                           [1]])
    weight['AND']['w1_w2'], weight['AND']['bias'] = learning(dataset, and_output)

    nand_output = np.array([[1],
                            [1],
                            [1],
                            [0]])
    weight['NAND']['w1_w2'], weight['NAND']['bias'] = learning(dataset, nand_output)

    or_output = np.array([[0],
                          [0],
                          [0],
                          [1]])
    weight['OR']['w1_w2'], weight['OR']['bias'] = learning(dataset, or_output)

    print(f"weight = {weight}")
    # weight = {
    #     'AND': {
    #         'w1_w2': array([[0.3],
    #                         [0.5]]),
    #         'bias': array([[-0.7]])
    #     },
    #     'NAND': {
    #         'w1_w2': array([[-0.4],
    #                         [-0.7]]),
    #         'bias': array([[1.]])
    #     },
    #     'OR': {
    #         'w1_w2': array([[0.4],
    #                         [0.4]]),
    #         'bias': array([[-0.7]])
    #     }
    # }