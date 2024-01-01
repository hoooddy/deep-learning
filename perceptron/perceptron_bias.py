import random
import pandas as pd

def perceptron(w1,x1, w2,x2, bias):
    result = (w1 * x1) + (w2 * x2) + bias

    if result <= 0:
        return 0
    elif result > 0:
        return 1


def learning(truth_table_df):
    while True:
        w1 = random.randint(-9, 9)/10
        w2 = random.randint(-9, 9)/10
        bias = random.randint(-9, 9)/10

        # 데이터 프레임의 한 행씩 반복 -> 진리표의 한 행씩 반복
        for index, row in truth_table_df.iterrows():
            if row['y'] != perceptron(w1, row['x1'], w2, row['x2'], bias):
                break
            if index == 3:
                return w1, w2, bias


def AND(truth_table_dict):
    truth_table_dict['y'] = [0, 0, 0, 1]
    truth_table_dict['type'] = 'AND'
    truth_table_df = pd.DataFrame(truth_table_dict)

    w1, w2, bias = learning(truth_table_df)

    print(f"[AND] w1: {w1}, w2: {w2}, bias: {bias}")


def NAND(truth_table_dict):
    truth_table_dict['y'] = [1, 1, 1, 0]
    truth_table_dict['type'] = 'NAND'
    truth_table_df = pd.DataFrame(truth_table_dict)

    w1, w2, bias = learning(truth_table_df)

    print(f"[NAND] w1: {w1}, w2: {w2}, bias: {bias}")


def OR(truth_table_dict):
    truth_table_dict['y'] = [0, 1, 1, 1]
    truth_table_dict['type'] = 'OR'
    truth_table_df = pd.DataFrame(truth_table_dict)

    w1, w2, bias = learning(truth_table_df)

    print(f"[OR] w1: {w1}, w2: {w2}, bias: {bias}")


if __name__ == '__main__':
    truth_table_dict = {'x1': [0, 1, 0, 1],
                        'x2': [0, 0, 1, 1]}

    AND(truth_table_dict)
    NAND(truth_table_dict)
    OR(truth_table_dict)

    """
    [AND] w1: 0.8, w2: 0.3, bias: -0.9
    [NAND] w1: -0.8, w2: -0.6, bias: 0.9
    [OR] w1: 0.5, w2: 0.6, bias: -0.1
    """