"""
Предложите решение для вычисления абсолютной
разницы между двумя целыми числами, a и b, используя только
побитовые операторы и основные арифметические операции
"""

class AbsoluteDifferenceCalculator:
    def calculate_absolute_difference(self, a, b):
        mask = 0xFFFFFFFF #32- bit

        while b:
            a, b = (a^b) & mask, ((a&b)<< 1) & mask

        return a if a <= 0x7FFFFFFF else ~ (a ^ mask)

b = AbsoluteDifferenceCalculator()
print(b.calculate_absolute_difference(5,2))