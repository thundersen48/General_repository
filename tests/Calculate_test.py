from unittest import TestCase, main
from calculate import calculate
class CalculatorTest(TestCase):

    def setUp(self) -> None:
        self.allowed = '+-/*'
    def test_plus(self):
        self.assertEqual(calculate('2+2'),4) #Проверяем равенство

    def test_minus(self):
        self.assertEqual(calculate('2-2'),0)

    def test_multiply(self):
        self.assertEqual(calculate('4*2'),8)
#Обработка исключения деления на ноль
    def test_division(self):
        self.assertEqual(calculate('2/2'),1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = 2/0

if __name__ == '__main__':
    main()