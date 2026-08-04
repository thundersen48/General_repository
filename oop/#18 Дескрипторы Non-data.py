#Дескрипторы - атрибут какого-то объекта, этот атрибут является объектом класса, тот класс у которого определнны методы сет, гет, делит
from random import choice
from time import time

class Epoch:
    def __get__(self,instance,owner_class):
        return int(time())

class Mytime:
    epoch = Epoch()

m = Mytime()
#print(m.epoch)

class Dice:
    @property
    def number(self):
        return choice(range(1,7)) # Choise выбирает рандомный элемент
                                  #Из последовательности
class Game:
    @property
    def rock_paper_scissors(self):
        return choice(['Rock','Paper','Scissors'])
    @property
    def flip(self):
        return choice(['Heads','Tails'])

    @property
    def dice(self):
        return choice(range(1, 7))


d = Game()

for i in range(3):
    d.dice
for i in range(3):
    print(d.dice)

