import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series([3, 8, 9, 0, 7])
print(obj)
print(obj.values)
print(obj.index)

obj2 = pd.Series([3, 8, -9, 0, -7], index=['a', 'b', 'c', 'e', 'd'])
print(obj2)
print(obj2.index)
print(obj2['b'])
obj2['e'] = 6
print(obj2[['c', 'e', 'd']])

print(obj2 > 0)
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

print(-7 in obj2)
print(-7 in obj2.values)
print('e' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())
print(obj4.notnull())

print(obj3 + obj4)

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)


print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan', 'Kate']
print(obj)
print('-----------------------------------------------')

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head())
print(frame.tail())
print(pd.DataFrame(data, columns=['year', 'pop', 'state']))

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four','five', 'six'])
print(frame2)
print(frame2.columns)
print(frame2['state'])
print(frame2.year)

print(frame2)
print(frame2.loc['three'])
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(6.)
print(frame2)

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
print(frame2.eastern)
del frame2['eastern']
print(frame2)

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
print(frame3.T)
print('-----------------------------------')
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
print(frame3)
print(pd.DataFrame(pdata))

frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
print(frame3.values)
print(frame3.index)
print(frame3.columns)

print(frame2.values)

obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
labels = pd.Index(np.arange(3))
print(labels)
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
print(obj2.index is labels)

print(frame3)
print(frame3.columns)
print('Ohio' in frame3.columns)
print(2002 in frame3.index)

dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(dup_labels)
