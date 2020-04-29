
import numpy as np
import os
import create_image as im

def data_fixed_x(n_data, x_values, set_functions, x_size, y_size, save_file):
    for i in range(n_data):
        for j, function in enumerate(set_functions):
            current_file = os.path.join(save_file,'_'.join(('dataset',str(j),str(i))))
            im.plot_image(function(x_values), x_values, x_size, y_size, save_file=current_file)
    



if __name__ == '__main__':
    x_values = np.linspace(0,100)/10
    set_functions = [lambda x: np.sin(x),
                    lambda x: np.cos(x)]
    data_fixed_x(2, x_values, set_functions, 15, 10,'dataset')