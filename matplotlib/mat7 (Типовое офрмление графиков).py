import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
plt.figtext(0.05, 0.6, 'Текст в области окна')
fig.suptitle('Заголовок окна')
ax.set_xlabel('Ox')
ax.set_ylabel('Oy')

ax.text(0.05, 0.1, 'Произвольный текст в координатных осях')
ax.annotate('Аннотация', xy=(0.2, 0.4), xytext=(0.6, 0.7),
            arrowprops={'facecolor': 'gray', 'shrink': 0.1})

plt.show()
"""
alpha степень прозрачности (число в диапазоне [0; 1])
backgroundcolor цвет фона
color или c цвет текста
fontfamily или family тип шрифта
fontsize или size размер шрифта
fontstyle или style стиль шрифта: {'normal', 'italic', 'oblique'}
fontweight или weight степень утолщения – число от 0 до 1000 или константы: 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'
horizontalalignment или ha выравнивание по горизонтали: {'center', 'right', 'left'}
label текст заголовка
position координаты текста (x, y)
rotation поворот текста: вещественное число [0; 1] или константы {'vertical', 'horizontal'}
verticalalignment или va выравнивание по вертикали: {'center', 'top', 'bottom', 'baseline', 'center_baseline'}
visible отображение текста: True/False
x координата x – вещественное число [0; 1]
y координата y – вещественное число [0; 1]
"""