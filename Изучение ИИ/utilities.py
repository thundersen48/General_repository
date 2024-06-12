import numpy as np
import matplotlib.pyplot as plt
#Определение для Х и У минимального и максимального
# значений, которые будут использоваться при построении сетки
def visualize_classifier(classifier, x, y):
    min_x,max_x = x[:, 0].min() - 1.0, x[:, 0].max() + 1.0
    min_y, max_y = x[:, 1].min() - 1.0, x[:, 1].max() + 1.0

mesh_step_size = 0.01

x_vals, y_vals = np.meshgrid(np.arange(min_x, max_x,mesh_step_size), np.arange(min_y, max_у, mesh_step_size))

output = classifier.predict(np.c_[x_vals.ravel(),y_vals.ravel()])