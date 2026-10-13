import numpy as np

y= 45

Az = np.array([[np.cos(y), np.sin(y), 0 ],[-np.sin(y), np.cos(y),0],[0,0,1]])

r1 = np.array([int(input('Введите значение x: ')), int(input('Введите значение y: ')), int(input('Введите значение z: '))])
r2 = np.dot(Az, r1)

print(f'Координаты токи r2: {r2}')
