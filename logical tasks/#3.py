"""
Задача: Проверить является ли число из списка целым!
"""
""" функция isprime()"""

class PrimeCounter:
    def count_primes(self, num):
        if num < 2:
            return 0

        is_prime = [True] * (num + 1)# Инициализация списка размером num + 1, гле каждый элемент представляет является ли число простым
        is_prime[0] = is_prime[1] = False # Устанавливаем False на 0 и 1 поскольку не являются простыми
#Цикл повторяется до тех пор, пока i не достигнет квадратного корня из num
        for i in range(2, int(num**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, num + 1, i): # Суммируем истинные значения в списке, чтобы получить кол-во простых чисел в заданом диапазоне
                    is_prime[j] = False

        return sum(is_prime)

solve = PrimeCounter()
print(solve.count_primes(num=20))
