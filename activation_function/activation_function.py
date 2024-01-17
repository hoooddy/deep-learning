import numpy as np
import matplotlib.pylab as plt
import os


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
    return np.maximum(0, a)


def activation_function_example(activation_function, activation_function_title):
    x_list = [-0.1, 0.1]
    for a in x_list:
        print(f"{activation_function_title}({a}) = {activation_function(a=a)}")


def draw_graph(activation_function, graph_title):
    x = np.arange(-5.0, 5.0, 0.1)
    y = activation_function(a=x)

    plt.title(graph_title)
    plt.plot(x, y)

    plt.savefig(f"graph/{graph_title}.png")


if __name__ == "__main__":
    if not os.path.exists("graph"):
        os.makedirs("graph")

    activation_function_example(step_function, "step_function")
    draw_graph(step_function, "Step_Function")

    activation_function_example(sigmoid, "sigmoid")
    draw_graph(sigmoid, "Sigmoid")

    activation_function_example(tanh, "tanh")
    draw_graph(tanh, "Tanh")

    activation_function_example(relu, "relu")
    draw_graph(relu, "ReLU")
