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


def get_truth_table(truth_table_dict, y, type):
    truth_table_dict['y'] = y
    truth_table_dict['type'] = type
    return pd.DataFrame(truth_table_dict)


if __name__ == '__main__':
    truth_table_dict = {'x1': [0, 1, 0, 1],
                        'x2': [0, 0, 1, 1]}

    weight = {
        'AND': {},
        'NAND': {},
        'OR': {}
    }

    # AND 연산 학습
    and_truth_table = get_truth_table(truth_table_dict, [0, 0, 0, 1], 'AND')
    weight['AND']['w1'], weight['AND']['w2'], weight['AND']['bias'] = learning(and_truth_table)

    # NAND 연산 학습
    nand_truth_table = get_truth_table(truth_table_dict, [1, 1, 1, 0], 'NAND')
    weight['NAND']['w1'], weight['NAND']['w2'], weight['NAND']['bias'] = learning(nand_truth_table)

    # OR 연산 학습
    or_truth_table = get_truth_table(truth_table_dict, [0, 1, 1, 1], 'OR')
    weight['OR']['w1'], weight['OR']['w2'], weight['OR']['bias'] = learning(or_truth_table)

    print(f"weight = {weight}")
    """weight = {
        'AND': {
            'w1': 0.2, 'w2': 0.7, 'bias': -0.8
        },
        'NAND': {
            'w1': -0.6, 'w2': -0.3, 'bias': 0.8
        },
        'OR': {
            'w1': 0.6, 'w2': 0.7, 'bias': -0.3
        }
    }"""