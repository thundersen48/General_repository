import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

x = np.array([[0.1, 1.0, 22.8],
               [0.5, 5.0, 41.2],
               [1.2, 12.0, 2.8],
               [0.8, 8.0, 14.0]])

roles = np.array([('Tom', 'manager'),
                   ('Mary', 'developer'),
                   ('Ann', 'recruiter'),
                   ('Jim', 'developer')])
encoder = OneHotEncoder()
encoded_roles = encoder.fit_transform(roles[:, [1]])
print(encoded_roles.toarray())

print(x)
scaler = StandardScaler()
scaled_x = scaler.fit_transform(x)
print(scaler.scale_)
print(scaler.mean_)
print(scaler.var_)
print(scaled_x.mean(axis=0))
print(scaled_x.std(axis=0))
print(scaler.inverse_transform(scaled_x))