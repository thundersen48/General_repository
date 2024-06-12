def calculate(expession):
    allowed = '+-/*'
    if not any(sign in expession for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак {allowed}')

    for sign in allowed:
        if sign in expession:
            try:
                left, right = expession.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except ZeroDivisionError:
                print('Деление на ноль невозможно')
            except(ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и один знак')


if __name__ == '__main__':
    print(calculate('10/2'))
