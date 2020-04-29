import matplotlib.pyplot as plt
import numpy as np


def plot_image(ordonne_y, abscisse_x, x_size, y_size, save_file=None):
    fig, ax = plt.subplots(1, 1, figsize=(x_size, y_size))
    ax.plot(ordonne_y)
    ax.set_xticklabels(abscisse_x)
    if save_file is not None:
        plt.savefig(save_file)
    else:
        plt.show()


if __name__ == '__main__':
    x_values = np.linspace(0, 100)/10
    series = np.sin(x_values)
    plot_image(series, x_values, 15, 10)
