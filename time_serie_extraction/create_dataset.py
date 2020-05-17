import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import random
import numpy as np
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
    """Creates a dataset of images of time series with fixed x values.

    The size of the output image can be controlled.

    Args:
        x_values (ndarray): x-axis values.
        set_functions (list of function): fonctions to apply to x_values.
        x_size (float): x-size of the output image.
        y_size (float): y-size of the output image.
        save_factor(str): path to save directory.
        sub_name(str, optional): additionnal descirption added to 
            images names.

    Returns:
        None
    """
    targets = []
    names = []
    for j, function in tqdm(enumerate(set_functions)):
        tmp_name = ''.join((str(j),sub_name,".png"))
        tmp_target = function(x_values)
        targets.append(tmp_target)
        names.append(tmp_name)
        current_path = os.path.join(save_factor, "images", tmp_name)
        plot_image(tmp_target, x_values, x_size, y_size, save_path=current_path)
    df_target = pd.DataFrame(data={"name": names, x_values: targets})
    target_path = os.path.join(save_factor, "target.pkl")
    df_target.to_pickle(target_path)


def create_data_fixed_len(n_x, scale_x, set_functions, x_size, y_size, save_factor, sub_name=""):
    """Creates a dataset of images of time series with fixed x values.

    The size of the output image can be controlled.

    Args:
        n_x (int): number of x-axis values.
        scale_x (float): scale applied rescaling to x-values.
        set_functions (list of function): fonctions to apply to x_values.
        x_size (float): x-size of the output image.
        y_size (float): y-size of the output image.
        save_factor(str): path to save directory.
        sub_name(str, optional): additionnal descirption added to 
            images names.

    Returns:
        None
    """
    targets, x_values, names = [], [], []
    try:
        os.mkdir(os.path.join(save_factor,'images'))
    except:
        print('Over-writting an existing directory')
    for j, function in tqdm(enumerate(set_functions)):
        rnd_init = random.random()*scale_x
        rnd_step = random.random()*scale_x
        tmp_x_values = [rnd_init + rnd_step*i for i in range(n_x)]
        tmp_name = ''.join((str(j),sub_name,".png"))
        tmp_target = function(tmp_x_values)
        targets.append(tmp_target)
        x_values.append(tmp_x_values)
        names.append(tmp_name)
        current_path = os.path.join(save_factor, "images", tmp_name)
        plot_image(tmp_target, tmp_x_values, x_size, y_size, save_path=current_path)
    
    col_names = [''.join(('x_value_',str(i))) for i in range(n_x)].extend(
                [''.join(('y_value_',str(i))) for i in range(n_x)])
    data = np.concatenate((np.array(targets),
            np.array(x_values)),0)
    df = pd.DataFrame(data=data, columns=col_names)
    with open(os.path.join(save_factor,'target.csv'), 'a') as f:
        df.to_csv(f, header=f.tell()==0, sep=',', index=True)
    