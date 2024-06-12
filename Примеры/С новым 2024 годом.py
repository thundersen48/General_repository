import time
import random
import pyfiglet as pf
from pyfiglet import Figlet
from termcolor import colored

text = 'Happy New Year 2024'

color_list = ['red', 'green', 'blue', 'yellow']
data_list = []

with open('texts.txt') as f:
    data_list = [line.strip() for line in f]
happy = pf.figlet_format(text)
for i in range (0,1):
    if i % 2 == 0:
        f = Figlet(font= random.choice(data_list))
        text_art = colored(f.renderText(text), random.choice(color_list))
    else:
        text_art = happy
    print('/n', text_art)
