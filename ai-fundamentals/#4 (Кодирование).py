import numpy as np
from sklearn import preprocessing

#Представление меток входных данных
input_labels = ['red', 'blасk', 'red', 'green', 'black', 'yellow',
'white']

#Создадим субъект кодирования меток и обучим его
encoder = preprocessing.LabelEncoder()#Создание кодировщика и установления соответствия между метками и числами
encoder.fit(input_labels)
#Выводим отображения слов на числа
print("\nLabel mapping:")
for i, item in enumerate(encoder.classes_) :
    print(item, '-->', i)
#Преобразуем набор случайно упорядочненных меток, чтобы проверить работу кодировщика
test_labels = ["green", 'red', 'black']
encoded_values = encoder.transform(test_labels)
print('/nLabels =',test_labels)
print("Encoded values =", list(encoded_values ) )
#Декодируем случайный набор данных
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list (decoded_list))