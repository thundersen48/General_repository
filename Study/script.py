#!/usr/bin/env python3



L1 = ['Maks', 'John', 'Anastasiya']
"""
for i in range(len(L1)):
    # Проверяем, что текущий индекс не равен 0 (пропускаем Maks)
    if i != 2:
        print(f'Идем на ужин {L1[i]}')
    else:
        print(f'К сожалению гость {L1[i]} не придет')
    
    
L1.append('Guest')

print('Текущие гости:')
for i in range(len(L1)):
    print(f'{i+1}.{L1[i]}')
"""

"""
L1.insert(0,'Sergey')
L1.insert(3, 'Stepan')
L1.append('Mariana')
"""
"""
print('Гости которые придут на ужин:')
for i in range(len(L1)):
    print(f'{i+1}.{L1[i]}')


print('Гости которые не придут на ужин:')

for i in range(1, 1, -1):
    print(f'{L1.pop(i)}')
"""

print(f'К столу приглашаются всего 2 гостя: {L1[0]} и {L1[1]}, поэтому {L1.pop()} к сожалению не придут на ужин')
del L1[0:2]

print(f'Пустой список {L1}')
# %%
