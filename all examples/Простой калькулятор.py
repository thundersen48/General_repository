class Parser:
    def __init__(self):
        pass
#expression - Строка

    def __convert_type(self,value_str):
        result = 0
        if isinstance(value_str,str):
            if '.' in value_str:
                result = float(value_str)
            else:
                result = int(value_str)

            return result


    def parse(self, expression):
        packed_values = tuple(expression.split(' ')) # Разделяем значения по пробелу
        if len(packed_values) < 3:
            print('Не правильные отступы')
            return 0, '+', 0
        a, op,b = packed_values#Записываем результат tuple
        return self.__convert_type(a), self.__convert_type(b),op

class Core:
    def __init__(self):
        self._parser = Parser()
        self._functions = {
            "+": lambda a,b: a+b,# Передаем агрументы, затем выражение.
            "-": lambda a,b: a-b,
            "/": lambda a,b: a/b,
            "*": lambda a,b: a*b

        }

    def calculate(self, expression):
        a, b, op = self._parser.parse(expression)
        result = self._functions.get(op)(a, b)
        return result

#Интерфейс программы
class Interface:
    def __init__(self):
        self._core = Core()

    def run_calculator (self):
        while True:
            print("Введите выражение:")
            expression = input()
            result = self._core.calculate(expression)
            print('Result: {}'.format(result))
            print('='*10)

if __name__ == '__main__':
    calculator = Interface()
    calculator.run_calculator()
