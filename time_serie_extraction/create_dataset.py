import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import os


def plot_image(y_values, x_values, x_size, y_size, save_path=None):
    fig, ax = plt.subplots(1, 1, figsize=(x_size, y_size))
    ax.plot(x_values, y_values)
    if save_path is not None:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()


def create_data_fixed_x(x_values, set_functions, x_size, y_size, save_factor, sub_name=""):
    targets = []
    names = []
    for j, function in tqdm(enumerate(set_functions)):
        tmp_name = str(j) + sub_name + ".png"
        tmp_target = function(x_values)
        targets.append(tmp_target)
        names.append(tmp_name)
        current_path = os.path.join(save_factor, "images", tmp_name)
        plot_image(tmp_target, x_values, x_size, y_size, save_path=current_path)
    df_target = pd.DataFrame(data={"name": names, "target": targets})
    target_path = os.path.join(save_factor, "target.pkl")
    df_target.to_pickle(target_path)
