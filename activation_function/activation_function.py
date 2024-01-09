import numpy as np


def step_function(input_signal):
    # if input_signal <= 0:
    #     return 0
    # elif input_signal > 0:
    #     return 1

    return np.array(input_signal > 0, dtype=np.int32)


def sigmoid(input_signal):
    return 1 / (1 + np.exp(-input_signal))


if __name__ == "__main__":
    print(step_function(input_signal=-0.1))
    print(step_function(input_signal=0.1))

    print(sigmoid(input_signal=-0.1))
    print(sigmoid(input_signal=1))
