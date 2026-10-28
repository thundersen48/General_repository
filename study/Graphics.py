# Лабораторная работа № 3. Построение графиков (карты значений и линии регрессии).
# Запуск: python grafiki_lr3.py   (нужны пакеты numpy и matplotlib)
# Гистограммы строятся отдельно в Excel.

import numpy as np
import matplotlib.pyplot as plt

# ---------- Оформление: черно-белая гамма, шрифт Times New Roman ----------
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'Liberation Serif', 'DejaVu Serif']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 0.8

# ---------- Исходные данные (таблицы 1 и 2 протокола), HL ----------
# Строки - линии, столбцы - сечения I-IV
obr1 = np.array([[370, 385, 178, 186],
                 [445, 368, 297, 177],
                 [404, 376, 202, 175],
                 [397, 363, 186, 187],
                 [451, 411, 218, 218],
                 [503, 381, 207, 198],
                 [527, 416, 190, 285],
                 [339, 365, 230, 221]])
obr2 = np.array([[230, 305, 409, 374], [362, 386, 485, 484], [180, 290, 308, 288],
                 [204, 354, 398, 387], [287, 447, 504, 479], [191, 338, 355, 389],
                 [172, 350, 356, 374], [290, 439, 486, 490], [216, 320, 351, 397],
                 [173, 355, 385, 444], [280, 400, 487, 491], [188, 286, 365, 409]])
sechenia = ['I', 'II', 'III', 'IV']


# ---------- Карта значений твердости ----------
def karta(dannye, imya_fayla, vysota):
    fig, ax = plt.subplots(figsize=(5.0, vysota), dpi=300)
    ax.imshow(dannye, cmap='Greys', vmin=100, vmax=620, aspect='auto')
    # значение в каждой ячейке (на темном фоне - белым цветом)
    for i in range(dannye.shape[0]):
        for j in range(dannye.shape[1]):
            cvet = 'white' if dannye[i, j] > 330 else 'black'
            ax.text(j, i, str(dannye[i, j]), ha='center', va='center', color=cvet, fontsize=11)
    ax.set_xticks(range(4))
    ax.set_xticklabels(sechenia)
    ax.set_yticks(range(dannye.shape[0]))
    ax.set_yticklabels(range(1, dannye.shape[0] + 1))
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.set_xlabel('Сечение')
    ax.set_ylabel('Линия')
    # белая сетка между ячейками
    ax.set_xticks(np.arange(-0.5, 4, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, dannye.shape[0], 1), minor=True)
    ax.grid(which='minor', color='white', linewidth=1.2)
    ax.tick_params(which='minor', length=0)
    fig.tight_layout()
    fig.savefig(imya_fayla)
    plt.close(fig)


# ---------- Регрессия твердости в сечении I по номеру линии ----------
def regressiya(dannye, imya_fayla):
    y = dannye[:, 0].astype(float)          # твердость в сечении I
    n = len(y)
    x = np.arange(1, n + 1, dtype=float)    # номер линии
    # коэффициенты по тем же формулам, что в отчете
    x_sr, y_sr = x.mean(), y.mean()
    b1 = ((x * y).mean() - x_sr * y_sr) / ((x ** 2).mean() - x_sr ** 2)
    b0 = y_sr - b1 * x_sr
    print(f'n = {n}: b0 = {b0:.2f}, b1 = {b1:.3f}')

    fig, ax = plt.subplots(figsize=(6.0, 3.6), dpi=300)
    ax.scatter(x, y, color='black', s=26, zorder=3, label='Измеренные значения')
    ax.plot([1, n], [b0 + b1 * 1, b0 + b1 * n], color='black', linewidth=1.2, label='Линия регрессии')
    ax.set_xticks(x)
    ax.set_xlabel('Номер линии x')
    ax.set_ylabel('Твердость H, HL')
    ax.grid(True, linewidth=0.4, color='#999999')
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=11)
    fig.tight_layout()
    fig.savefig(imya_fayla)
    plt.close(fig)


karta(obr1, 'karta_obr1.png', 3.6)
karta(obr2, 'karta_obr2.png', 5.0)
regressiya(obr1, 'regressiya_obr1.png')
regressiya(obr2, 'regressiya_obr2.png')
print('Готово')
