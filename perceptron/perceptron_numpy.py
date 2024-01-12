import numpy as np
import random


def perceptron(x1, w1, x2, w2, b):
    a = x1 * w1 + x2 * w2 + b

    if a <= 0:
        return 0
    elif a > 0:
        return 1


def learning(x, y):
    # random.randint: [low, high) = low 이상, high 미만
    check = 0
    while True:
        w1 = np.random.randint(-10, 11, (1, 1)) / 10
        w2 = np.random.randint(-10, 11, (1, 1)) / 10
        b = np.random.randint(-10, 11, (1, 1)) / 10

        result = np.empty((0, 1))

        for x1, x2 in x:
            result = np.append(result, np.array([[perceptron(x1, w1, x2, w2, b)]]), axis=0)

        if (result == y).all():
            return w1, w2, b


def xor(x, w1_w2):
    xor_result = np.empty((0, 1))

    for x1, x2 in x:
        nand_result = perceptron(x1, w1_w2['NAND']['w1'],
                                 x2, w1_w2['NAND']['w2'],
                                 w1_w2['NAND']['bias'])
        or_result = perceptron(x1, w1_w2['OR']['w1'],
                               x2, w1_w2['OR']['w2'],
                               w1_w2['OR']['bias'])

        and_result = perceptron(nand_result, w1_w2['AND']['w1'],
                                or_result, w1_w2['AND']['w2'],
                                w1_w2['AND']['bias'])

        xor_result = np.append(xor_result, np.array([[and_result]]), axis=0)

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
    weight['AND']['w1'], weight['AND']['w2'], weight['AND']['bias'] = learning(dataset, and_output)

    # NAND 연산 학습
    nand_output = np.array([[1],
                            [1],
                            [1],
                            [0]])
    weight['NAND']['w1'], weight['NAND']['w2'], weight['NAND']['bias'] = learning(dataset, nand_output)

    # OR 연산 학습
    or_output = np.array([[0],
                          [1],
                          [1],
                          [1]])
    weight['OR']['w1'], weight['OR']['w2'], weight['OR']['bias'] = learning(dataset, or_output)

    print(f"weight = {weight}")
    # weight = {
    #     'AND': {
    #         'w1': array([[0.3]]),
    #         'w2': array([[0.5]]),
    #         'bias': array([[-0.7]])
    #     },
    #     'NAND': {
    #         'w1': array([[-0.9]]),
    #         'w2': array([[-0.6]]),
    #         'bias': array([[1.]])
    #     },
    #     'OR': {
    #         'w1': array([[1.]]),
    #         'w2': array([[0.8]]),
    #         'bias': array([[-0.5]])}
    # }

    # XOR 연산
    xor_output = np.array([[0],
                           [1],
                           [1],
                           [0]])
    xor_result = xor(dataset, weight)

    print(f"xor_result: {xor_result}")
    print(f"result: {(xor_output == xor_result).all()}")
    # xor_result: [[0.]
    #              [1.]
    #              [1.]
    #              [0.]]
    # result: True

