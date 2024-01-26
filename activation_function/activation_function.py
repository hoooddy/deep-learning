import numpy as np


def step_function(a):
    # if a <= 0:
    #     return 0
    # elif a > 0:
    #     return 1

    return np.array(a > 0, dtype=np.int32)


def sigmoid(a):
    return 1 / (1 + np.exp(-a))


def tanh(a):
    return (np.exp(a) - np.exp(-a))/(np.exp(a) + np.exp(-a))


def relu(a):
    return np.maximum(0, a)


def leaky_relu(a):
    return np.maximum(0.01*a, a)
