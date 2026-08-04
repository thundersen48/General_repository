

print('____Автоматические ворота____')
is_open = False # Изначально закрыли ворота
while True:
    command = input('command:').lower()
    if command == 'open':
        if is_open:
            print('Ворота уже открыты')
        else:
            print('Opening...')
        is_open = True
    elif command =='close':
        if is_open:
            print('closing...')
        else:
            print('Ворота уже закрыты.')
        is_open = False
    elif command == 'help':
        print("""help menu:
        open: открывает ворота
        close: закрывает ворота
        stop: Останавливает программу""")
    elif command =='stop':
        print('Stopping...')
        break
    else:
        print('Incorrect command.')
    print('Stopped.')

