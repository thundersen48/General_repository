import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()
x = ['Математика', 'Физика', 'Русский ','Английский']
y = [40, 65, 70 ,30]

plt.xlabel('Дисциплины',color='Black',weight=1)
plt.title('Успеваемость',color='red',weight=2)

ax.set_ylabel('Уровень')
plt.bar(x,y, color='green', align='edge',width=0.5)# начерти столбчатую диаграмму

plt.show()