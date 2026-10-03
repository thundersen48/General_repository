import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


# ------------------------- 1. Загрузка данных -------------------------
def load_oscillograms_from_folder(folder_path):
    """
    Читает все текстовые файлы из папки.
    Каждый файл содержит два столбца: время и ток (разделитель ';').
    Возвращает массив numpy формы (n_oscillograms, 512).
    """
    data = []
    for fname in os.listdir(folder_path):
        if fname.endswith('.txt'):
            filepath = os.path.join(folder_path, fname)
            df = pd.read_csv(filepath, sep=';', header=None, names=['t', 'I'])
            # Берём только значения тока (512 отсчётов)
            current = df['I'].values
            if len(current) != 512:
                # Если файл короче – дополняем нулями (на всякий случай)
                current = np.pad(current, (0, max(0, 512 - len(current))), constant_values=0)
            data.append(current[:512])
    return np.array(data)


# Укажите пути к папкам с осциллограммами для двух классов
# В данном примере файлы oscillogram_1..5.txt лежат в папке 'class1',
# а oscillogram_4,5,1,2,3.txt (второй набор) – в папке 'class2'.
# Замените на свои пути.
PATH_CLASS1 = 'M:\Projects\pythonM\Учеба РУТ МИИТ\Classifier\class1'  # сюда положите первые 5 файлов (1..5)
PATH_CLASS2 = 'M:\Projects\pythonM\Учеба РУТ МИИТ\Classifier\class2'  # сюда положите вторые 5 файлов (4,5,1,2,3)

X_class1 = load_oscillograms_from_folder(PATH_CLASS1)
X_class2 = load_oscillograms_from_folder(PATH_CLASS2)

print(f"Загружено осциллограмм: класс1 = {X_class1.shape[0]}, класс2 = {X_class2.shape[0]}")

# Объединяем данные и создаём метки
X = np.vstack([X_class1, X_class2])
y = np.hstack([np.zeros(X_class1.shape[0]), np.ones(X_class2.shape[0])])

# ------------------------- 2. Визуализация (по одному примеру из каждого класса) -------------------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(X_class1[0], color='blue')
plt.title('Осциллограмма класса 1 (потребитель №1)')
plt.xlabel('Номер отсчёта')
plt.ylabel('Ток, отн. ед.')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(X_class2[0], color='red')
plt.title('Осциллограмма класса 2 (потребитель №2)')
plt.xlabel('Номер отсчёта')
plt.ylabel('Ток, отн. ед.')
plt.grid(True)

plt.tight_layout()
plt.savefig('oscillograms.png', dpi=150)
plt.show()


# ------------------------- 3. Извлечение признаков -------------------------
def extract_features(signal):
    """
    Извлекает признаки из осциллограммы:
    - статистические: среднее, дисперсия, асимметрия, эксцесс, СКЗ, максимум
    - частотные: первые 20 модулей БПФ
    """
    mean_val = np.mean(signal)
    var_val = np.var(signal)
    # Асимметрия и эксцесс через моменты 3 и 4 порядка
    n = len(signal)
    m3 = np.mean((signal - mean_val) ** 3)
    skew = m3 / (var_val ** 1.5) if var_val > 0 else 0
    m4 = np.mean((signal - mean_val) ** 4)
    kurt = m4 / (var_val ** 2) - 3 if var_val > 0 else 0

    rms = np.sqrt(np.mean(signal ** 2))
    max_abs = np.max(np.abs(signal))

    # БПФ – берём модули первых 20 коэффициентов (кроме постоянной составляющей)
    fft_vals = np.abs(np.fft.rfft(signal))[1:21]  # 20 значений

    features = np.concatenate(([mean_val, var_val, skew, kurt, rms, max_abs], fft_vals))
    return features


X_features = np.array([extract_features(sig) for sig in X])
print(f"Размерность признакового пространства: {X_features.shape[1]}")

# ------------------------- 4. Нормализация, разделение выборки -------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_features)

# Разделение на обучающую (80%) и тестовую (20%) с сохранением пропорции классов
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Обучающая выборка: {X_train.shape[0]} примеров, тестовая: {X_test.shape[0]}")

# ------------------------- 5. Обучение MLP-классификатора -------------------------
mlp = MLPClassifier(
    hidden_layer_sizes=(128, 128),  # два скрытых слоя по 128 нейронов
    activation='relu',
    solver='adam',
    alpha=0.0001,
    batch_size=32,
    learning_rate='adaptive',
    max_iter=500,
    early_stopping=True,
    validation_fraction=0.1,
    random_state=42
)

mlp.fit(X_train, y_train)

# ------------------------- 6. Оценка качества -------------------------
y_pred = mlp.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n=== Результаты классификации ===")
print(f"Accuracy (доля правильных ответов):  {accuracy:.4f}")
print(f"Precision (точность):                {precision:.4f}")
print(f"Recall (полнота):                    {recall:.4f}")
print(f"F1-score (F-мера):                   {f1:.4f}")
print("\nМатрица ошибок (confusion matrix):")
print(confusion_matrix(y_test, y_pred))

# Дополнительно: если F1 < 0.95, можно изменить архитектуру – здесь это демонстрация
if f1 < 0.95:
    print("\nВнимание: F-мера ниже 0.95. Рекомендуется увеличить датасет до 1000 осциллограмм,")
    print("или изменить архитектуру классификатора (например, добавить слой, увеличить число нейронов).")
else:
    print("\nТребование F1 >= 0.95 выполнено!")