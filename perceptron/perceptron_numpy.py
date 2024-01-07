# import numpy as np
# import random
#
# def perceptron(x1, w1, x2, w2, b):
#     result = x1 * w1 + x2 * w2 + b
#
#     if result <= 0:
#         return 0
#     elif result > 0:
#         return 1
#
#
# def learning(x, y):
#     # random.randint: [low, high) = low 이상, high 미만
#     check = 0
#     while True:
#         w = np.random.randint(-10, 11, (4, 2)) / 10
#         b = np.random.randint(-10, 11, (1, 1)) / 10
#
#         result = np.array([[]])
#         for x, w in zip(x, w):
#             result = np.append(result, [perceptron(x[0], w[0], x[1], w[1], b)], axis=1)
#             print(result)
#         print(f"learning result: {result}")
#         if (result == y).all():
#             return w[0], w[1], b
#
#
# def xor(x, w1_w2):
#     xor_result = np.array([])
#     for x1, x2 in x:
#         nand_result = perceptron(x1, w1_w2['NAND']['w1'],
#                                  x2, w1_w2['NAND']['w2'],
#                                  w1_w2['NAND']['bias'])
#         or_result = perceptron(x1, w1_w2['OR']['w1'],
#                                x2, w1_w2['OR']['w2'],
#                                w1_w2['OR']['bias'])
#         print(nand_result, or_result)
#         and_result = perceptron(nand_result, w1_w2['AND']['w1'],
#                                 or_result, w1_w2['AND']['w2'],
#                                 w1_w2['AND']['bias'])
#         print(f"and_result: {and_result}")
#         np.append(xor_result, [and_result])
#     print(xor_result)
#     return xor_result
#
#
# if __name__ == '__main__':
#     dataset = np.array([[0, 0],
#                         [1, 0],
#                         [0, 1],
#                         [1, 1]])
#
#     # # 'AND', 'NAND', 'OR' 연산을 위한 가중치
#     weight = {
#         'AND': {},
#         'NAND': {},
#         'OR': {}
#     }
#
#     # AND 연산 학습
#     and_output = np.array([[0],
#                            [0],
#                            [0],
#                            [1]])
#     weight['AND']['w1'], weight['AND']['w2'], weight['AND']['bias'] = learning(dataset, and_output)
#
#     # NAND 연산 학습
#     nand_output = np.array([[1],
#                             [1],
#                             [1],
#                             [0]])
#     weight['NAND']['w1'], weight['NAND']['w2'], weight['NAND']['bias'] = learning(dataset, nand_output)
#
#     # OR 연산 학습
#     or_output = np.array([[0],
#                           [1],
#                           [1],
#                           [1]])
#     weight['OR']['w1'], weight['OR']['w2'], weight['OR']['bias'] = learning(dataset, or_output)
#
#     print(f"weight = {weight}")
#     # weight = {
#     #     'AND': {
#     #         'w1_w2': array([[0.9],
#     #                         [0.4]]),
#     #         'bias': array([[-1.]])
#     #     },
#     #     'NAND': {
#     #         'w1_w2': array([[-0.6],
#     #                         [-0.7]]),
#     #         'bias': array([[1.]])
#     #     },
#     #     'OR': {
#     #         'w1_w2': array([[0.9],
#     #                         [1.]]),
#     #         'bias': array([[-0.7]])
#     #     }
#     # }
#
#     # XOR 연산
#     xor_output = np.array([[0],
#                            [1],
#                            [1],
#                            [0]])
#     xor_result = xor(dataset, weight)
#
#     print(f"xor_result: {xor_result}")
#     print(f"result: {(xor_output == xor_result).all()}")
#     # xor_result: [[0]
#     #              [1]
#     #              [1]
#     #              [0]]
#     # result: True
