import pandas as pd
# pd.Series([1, '2','хуйня'])
# a = pd.Series([1, '2','хуйня'],index=['a','b','c'])
# print (a[a=='хуйня'])

# a = pd.Series(range(15))
# print( a[a>10])

# s = pd.Series({'a':[1,2],'b':[3,4],'c':[5,6]})
#
# s['a'][0]
# print(s)

import matplotlib.pyplot as plt
plt.title('График хуйни')
week = pd.Series({'Понедельник': 90, 'Вторник':76,'Среда': 50, 'Четверг':80,'Пятница':39,'Суббота':66,'Воскресенье':100})
plt.plot (week)
plt.show()



