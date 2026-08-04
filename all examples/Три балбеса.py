

names = ['Ларри', 'Керли', 'Мо']
message = 'Три балбеса: '

for index, name in enumerate(names):
    if index > 0:
        message += ' ,'
    if index == len(names) - 1:
        message += ' и '
    message += name
print(message)

def introduce_stooges(names):
    message = 'Три Умника: '
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1:
            message += f'Но {names[2]} дебил '
        message += name

    print(message)

introduce_stooges(['Макс', 'Степа','Захар'])
introduce_stooges(['Мо', 'Ларри', 'Шемп'])

