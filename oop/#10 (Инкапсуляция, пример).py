from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[092m'
RED = '\033[1;31m'

class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self._history = []#Создаем историю операций в виде пустого списка

    def _get_current_time(self):
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time() ])

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'Вы потратили {amount} денег')
            self.show_balance()
            self.history.append([-amount,self._get_current_time()])
        else:
            print('Недостаточно средств')

    def show_balance(self):
        print(f'Balance:{self.balance}')

    def show_history(self):#Создаем метод который будет показывать историю
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposit'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on '
                  f'{date.astimezone()}')


pytz.utc.localize(datetime.utcnow())
b = pytz.utc.localize(datetime.utcnow()).astimezone().isoformat()#Получаем ссылку на текущий часовой пояс
a = Account ('Maks', 0)

a.deposit(100)
a.withdraw(30)
a.show_history()