t = "лилила"

p = [0]*len(t)
j = 0
i  = 1

while i < len(t):
    if t[j] ==t[i]:
        p[i] = j+1
        i+= 1
        j+=1
    else:
        if j == 0:
            p[i] = 0;
            i+= 1
        else:
            j = p[j-1]

print(p)

"""Поиск образа в строке"""

a = "лилилось лилилась"
m = len(t)
n = len(a)

i = 0
j = 0
while i<n:
    if a[i] == t[j]:
        i+=1
        j+=1
        if j ==m:
            print('Образ найден')
            break

    else:
        if j>0:
            j = p[j-1]
        else:
            i+= 1
if i == n:
    print('Образ не найден')


def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)

    # Создаем префикс-функцию
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    # Поиск подстроки
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1


# Пример использования
text = "abcdeabcdeabcde"
pattern = "cde"
result = kmp_search(pattern, text)
if result != -1:
    print("Подстрока найдена в позиции", result)
else:
    print("Подстрока не найдена")
