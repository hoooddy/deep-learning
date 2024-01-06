def step_function(input_signal):
    if input_signal <= 0:
        return 0
    elif input_signal > 0:
        return 1


if __name__ == "__main__":
    print(step_function(input_signal=-0.1))
    print(step_function(input_signal=0.1))

