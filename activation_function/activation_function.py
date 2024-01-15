import numpy as np
import matplotlib.pylab as plt


def step_function(a):
    # if input_signal <= 0:
    #     return 0
    # elif input_signal > 0:
    #     return 1

    return np.array(a > 0, dtype=np.int32)


def sigmoid(a):
    return 1 / (1 + np.exp(-a))


def tanh(a):
    return (np.exp(a) - np.exp(-a))/(np.exp(a) + np.exp(-a))


def relu(a):
    if a >= 0:
        return 0
    else:
        return a


if __name__ == "__main__":
    print(step_function(a=-0.1))
    print(step_function(a=0.1))
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.show()

    print(sigmoid(a=-0.1))
    print(sigmoid(a=1))
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.show()

    print(tanh(a=-0.1))
    print(tanh(a=1))
    x = np.arange(-5.0, 5.0, 0.1)
    y = tanh(x)
    plt.plot(x, y)
    plt.show()

    print(relu(a=-0.1))
    print(relu(a=1))
