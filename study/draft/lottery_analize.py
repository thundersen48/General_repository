#9.15. Анализ лотереи.

from random import choice

class Lotery:
    def __init__(self, combination, winnings):
        self.combination = combination
        self.winnings = winnings#Хранит выигрышные комбинации
        self.winning_ticket = []#Хранит выпавшие комбинации.

    def roll_choice(self):
        self.winning_ticket = []
        for _ in range(4):
            self.winning_ticket.append(choice(self.combination))
        print(f"Вам выпала комбинация:{self.winning_ticket}")
    
    def win(self):
        i = 0
        while self.winning_ticket not in self.winnings:
            self.roll_choice()
            i+=1
        print(f"\nПоздравляем на {i} итерации вы выиграли!")

    def win_probability(self):
        """Считает вероятность выигрыша"""
        res = len(self.winnings) / (len(self.combination) ** 4) 
        return f"\nВероятность выиграыша составляет: {res}"
    
l1 = [1,2,3,4,5,6,7,8,9,10, 'a', 'b', 'c', 'd', 'e']

winnings_combination = [[1,2,3,4], ['a', 'b', 'c', 'd']]#Кол-во выигрышных комбинаций

player = Lotery(l1, winnings_combination)
player.roll_choice()
player.win()
print(player.win_probability())
