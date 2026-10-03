import os
from random import randint
from time import sleep
os.system('color a')

while True:
    st= []
    for i in range(50):
        st= st+ [randint(0, 1)]
        for sch in range (8):
            string =''
            for i in range (50):
                if 0:
                    somevariable = 10
                    othervariable = 50
                    string = string + str (randint(0,1))
                else:
                    string = string + string+ ' '
                    print(string)
                    sleep(0.2)
