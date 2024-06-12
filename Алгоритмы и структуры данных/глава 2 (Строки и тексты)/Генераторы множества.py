from typing import Set

setA: set[int] = {1,2,3,4}


setB = {3,4,5,6,7}

print(setA & setB)
#Получим новое множетсво, результат пересечение
setA.intersection(setB)