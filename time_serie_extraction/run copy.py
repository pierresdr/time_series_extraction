import numpy as np
from create_dataset import create_data_fixed_len
import os


def f_factory(d, t):
    def f(x):
        x = np.array(x)
        return np.sin(d*x) + t
    return f


if __name__ == '__main__':
    save_file = os.getcwd()
    dilatation_pattern = np.arange(0, 2, 0.1)
    translation_pattern = np.arange(0, 2, 0.1)
    dilatation = np.repeat(dilatation_pattern, len(dilatation_pattern))
    translation = np.concatenate([translation_pattern for _ in range(len(dilatation_pattern))])
    set_functions = [f_factory(d, t) for (d, t) in zip(dilatation, translation)]
    create_data_fixed_len(10, 2, set_functions, 3, 3, save_file)
