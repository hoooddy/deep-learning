import random
import pandas as pd

def perceptron(w1,x1, w2,x2, theta):
    result = (w1 * x1) + (w2 * x2)

    if result <= theta:
        return 0
    elif result > theta:
        return 1


def learning(truth_table_df):
    while True:
        w1 = random.randint(-9, 9)/10
        w2 = random.randint(-9, 9)/10
        theta = random.randint(-9, 9)/10

        for index, row in truth_table_df.iterrows():
            if row['y'] != perceptron(w1, row['x1'], w2, row['x2'], theta):
                break
            if index == 3:
                return w1, w2, theta


def AND(truth_table_dict):
    truth_table_dict['y'] = [0, 0, 0, 1]
    truth_table_dict['type'] = 'AND'
    truth_table_df = pd.DataFrame(truth_table_dict)

    w1, w2, theta = learning(truth_table_df)

    print(f"[AND] w1: {w1}, w2: {w2}, theta: {theta}")


def NAND(truth_table_dict):
    truth_table_dict['y'] = [1, 1, 1, 0]
    truth_table_dict['type'] = 'NAND'
    truth_table_df = pd.DataFrame(truth_table_dict)

    w1, w2, theta = learning(truth_table_df)

    print(f"[NAND] w1: {w1}, w2: {w2}, theta: {theta}")

def OR(truth_table_dict):
    truth_table_dict['y'] = [0, 1, 1, 1]
    truth_table_dict['type'] = 'OR'
    truth_table_df = pd.DataFrame(truth_table_dict)

    w1, w2, theta = learning(truth_table_df)

    print(f"[OR] w1: {w1}, w2: {w2}, theta: {theta}")


if __name__ == '__main__':
    truth_table_dict = {'x1': [0, 1, 0, 1],
                        'x2': [0, 0, 1, 1]}

    AND(truth_table_dict)
    NAND(truth_table_dict)
    OR(truth_table_dict)

    """
    [AND] w1: 0.9, w2: 0.6, theta: 0.9
    [NAND] w1: -0.7, w2: -0.4, theta: -0.8
    [OR] w1: 0.6, w2: 0.8, theta: 0.4
    """