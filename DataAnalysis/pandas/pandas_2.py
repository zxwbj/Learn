import numpy as np
import pandas as pd

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(7), method='ffill'))

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(frame)
print(frame.reindex(['b', 'c', 'a', 'd']))
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
print(frame.loc[['a', 'b', 'c', 'd'], states])
print(frame)
print('------------------------------------------')
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
print(obj.drop('c'))
print(obj.drop(['d', 'c']))

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data.drop(['Colorado', 'Ohio'], axis=0))
print(data.drop(['one', 'four'], axis=1))
print(data.drop(['one', 'three'], axis='columns'))
print(obj)
obj.drop('b', inplace=True)
print(obj)

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj[['b', 'a', 'd']])
print(obj[np.arange(3)])
print(obj[obj >= 2])
print(obj['b':'d'])
obj['b':'c'] = 5
print(obj)

print('----------------------------------------------')
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data['three'])
print(data[['three', 'one']])
print(data[:2])
print(data > 5)
print(data['three'] > 5)
print((data > 5)['three'])

data[data < 5] = 0
print(data)

print(data.loc['Colorado', ['two', 'three']])
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[[3, 0, 1], [1, 2]])
print(data)
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3])
print(data.iloc[:, :3][data.three > 5])

print('------------------------------')
ser = pd.Series(np.arange(3.))
print(ser)
# print(ser[-1])
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser2)
print(ser2[-1])

print(ser[:1])
print(ser.loc[:1])
print(ser.iloc[:1])
print('---------------------------------------------')
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
print(s1 + s2)
print('---------------------------------------')
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1 + df2)

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df2.loc[1, 'b'] = np.nan
print(df1)
print(df2)
print(df1 + df2)
print(df1.add(df2, fill_value=0))
print(1 / df1)
print(df1.rdiv(1))

arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr - arr[0])

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame)
print(series)
print(frame - series)

series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)

series3 = frame['d']
print(frame)
print(series3)
print(frame.sub(series3, axis='index'))
print('------------------------------------')

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))
print(np.max(frame))
print('--------------------------------------')

obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj)
print(obj.sort_index())
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame)
print(frame.sort_index(axis=0))
print(frame.sort_index(axis=1))
print(frame.sort_index(axis=1, ascending=False))

obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())

frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by='b'))
print( frame.sort_values(by=['a', 'b']))

obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
print(obj.rank(method='first'))
print(obj.rank(ascending=False, method='max'))

frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
print(frame.rank(axis='columns'))

obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)
print(obj.index.is_unique)
print(obj['a'])
print(obj['c'])

df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.loc['b'])
print('-----------------------------------------')
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)
print(df.sum())
print(df.sum(axis='columns'))
print(df.mean(axis='columns', skipna=False))
# print(df.idmax())
# print(df.idmin())
print(df.cumsum())
print(df.describe())

obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj)
print(obj.describe())

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
print(uniques)
uniques.sort()
print(uniques)
print(obj.value_counts())
print(pd.value_counts(obj.values, sort=False))

print(obj)
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])

to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
print(pd.Index(unique_vals).get_indexer(to_match))

data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                     'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
print(data)
result = data.apply(pd.value_counts).fillna(0)
print(result)


