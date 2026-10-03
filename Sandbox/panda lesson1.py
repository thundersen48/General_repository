import numpy
import pandas
import pandas as pd
a = pd.Series([3,-5,7,4], index = ['a','b','c','d'])

print(a)
dict_cities = {'City':['Moscow','Saint-Peterburg','Novosibirsk'],
               'Population':[12678079,5398064, 1625631]}
df = pd.DataFrame(dict_cities)
print(df)

list1=[['Moscow','Saint-Peterburg','Novosibirsk'],[12678079, 5398064, 1625631]]
f = pd.DataFrame(list1)
print(f)
#


