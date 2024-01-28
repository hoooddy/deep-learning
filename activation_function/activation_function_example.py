import matplotlib.pylab as plt
import os
from activation_function import *


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
    plt.clf()


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

    activation_function_example(leaky_relu, "leaky_relu")
    draw_graph(leaky_relu, "Leaky_ReLU")
