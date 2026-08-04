"""
Напишите программу, которая проверяет имя пользователя
на коррекность. Имя пользователя является правильным если
- в нем от 3 до 10 символов (len())
- все символы являются буквами .isalpha
-Первая буква прописная(верхний регистр)isupper()
- все остальные строчные
"""
username = input()
if 3<len(username)<=10 and\
        username.isalpha() and\
        username[0].isupper() and\
        username[1:].islower():
    print('Добро пожаловать')
elif len(username)<3 or len(username)>10:
    print('Проверьте ширину текста')
elif not username.isalpha():
    print('Проверьте! должны быть буквы!')
else:
    print('Пошел к черту')