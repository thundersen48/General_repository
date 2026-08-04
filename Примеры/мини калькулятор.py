def calculate (num1, num2, operator = '+'):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1-num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
    except ZeroDivisionError:
        print('Обратите внимание на нули')


num1 = int(input())
num2 = int(input())
operator = input()
result = calculate(num1, num2, operator)
print(result)
