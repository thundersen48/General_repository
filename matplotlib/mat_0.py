import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# 1. Сброс всех настроек в "заводские", чтобы убрать накопленные ошибки
plt.rcdefaults()

# 2. Твои параметры размеров
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)

# 3. Возвращаем чистый стиль Seaborn (он самый стабильный)
sns.set_theme(style="whitegrid") # Это современная замена старому set_style


# Проверка: нарисуй что-нибудь простое, чтобы убедиться, что сетка вернулась
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
