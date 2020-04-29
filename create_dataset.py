
import numpy as np
import os
import create_image as im


def dataset_fixed_x(n_data, x_values, set_functions, x_size, y_size, save_file):
    """
    Creates n_data plots for each of the set_functions over the fixed set of x_values
    """
    for i in range(n_data):
        for j, function in enumerate(set_functions):
            current_file = os.path.join(save_file,'_'.join(('dataset',str(j), str(i))))
            im.plot_image(function(x_values), x_values, x_size, y_size, save_file=current_file)


def dataset_random_x(n_data, n_x, set_functions, x_size, y_size, save_file):
    """
    Creates n_data plots for each of the set_functions over a random set of n_x values
    """
    for i in range(n_data):
        for j, function in enumerate(set_functions):
            x_values = np.random.random(size=n_x)
            x_values = np.cumsum(x_values)
            current_file = os.path.join(save_file,'_'.join(('dataset',str(j), str(i))))
            im.plot_image(function(x_values), x_values, x_size, y_size, save_file=current_file)


if __name__ == '__main__':
    set_functions = [lambda x: np.sin(x),
                    lambda x: np.cos(x)]
    dataset_random_x(2, 10, set_functions, 15, 10,'dataset')