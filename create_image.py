import matplotlib.pyplot as plt

def plot_image(series, x_values, x_size, y_size, save_file=None):
    fig, ax  = plt.subplots(1, 1, figsize=(x_size, y_size))
    ax.plot(series)
    ax.set_xticks(x_values)
    ax.set_xlabel(x_values)
    if save_file is not None:
        plt.savefig(save_file)
    else:
        plt.show()