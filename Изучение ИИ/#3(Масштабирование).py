import numpy as np
from sklearn import preprocessing

input_data = np.array([ [5.1, -2.9, 3.3],
[-1.2, 7.8, -6.1],
[3.9, 0.4, 2.1],
[7.3, -9.9, -4.5]])
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nМin max scaled data:\n", data_scaled_minmax)
#Каждая строка масштабируется так, чтобы максимальным значением было 1 а все остальные определялись относительно него.
#------------Нормализация данных---------
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nLl normalized data:\n", data_normalized_l1)#l1 - Наименьшие абсолютные отклонения
print("\n12 normalized data:\n", data_normalized_l2)#l2 - 