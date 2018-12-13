import numpy as np
import pandas as pd

data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(data)
print(data['a'][2])
print(data['d'][3])
print(data['c'])
print(data.index)

print(data)
print(data.unstack())
print(data.unstack().stack())

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
print(frame)
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print(frame['Ohio'])
print(frame['Colorado'])

print(frame.swaplevel('key1', 'key2'))
print(frame.sort_index(level=1))
print(frame.swaplevel(0, 1).sort_index(level=0))

print(frame)
print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))
print('-----------------------------------------------')
frame = pd.DataFrame({'a': range(7),
                      'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)
frame2 = frame.set_index(['c', 'd'])
print(frame2)
print(frame.set_index(['c', 'd'], drop=False))
print(frame2.reset_index())

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df1)
print(df2)
print(pd.merge(df1, df2))

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df3)
print(df4)
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))
print(pd.merge(df1, df2, how='outer'))

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})
print(pd.merge(df1, df2))
print(pd.merge(df1, df2, how='inner'))
print(pd.merge(df1, df2, on='key', how='left'))

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(pd.merge(left1, right1, left_on='key', right_index=True))
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio','Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
print(lefth)
print(righth)
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])
another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York', 'Oregon'])
print(another)
print(left2.join([right2, another]))

arr = np.arange(12).reshape((3, 4))
print(arr)
print(np.concatenate([arr, arr], axis=1))

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
print(pd.concat([s1, s2, s3]))
print(pd.concat([s1, s2, s3], axis=1))
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result)
print(result.unstack())
print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))
print('-----------------------------------------------')

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
print(a)
print(b)
print(np.where(a.isnull(), b, a))
print(b[:-2].combine_first(a[2:]))

df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                    'b': [np.nan, 2., np.nan, 6.],
                    'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                    'b': [np.nan, 3., 4., 6., 8.]})
print(df1)
print(df2)
print(df1.combine_first(df2))

data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)
print(data.stack())
print(data.stack().unstack())

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
print(data2)
print(data2.unstack())
print(data2.unstack().stack())
print(data2.unstack().stack(dropna=False))

data = pd.read_csv('examples/macrodata.csv')
print(data.head())
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata[:10])
pivoted = ldata.pivot('date', 'item', 'value')
print(pivoted)
ldata['value2'] = np.random.randn(len(ldata))
print(ldata[:10])
pivoted = ldata.pivot('date', 'item')
print(pivoted[:5])
print(pivoted['value'][:5])

unstacked = ldata.set_index(['date', 'item']).unstack('item')
print(unstacked[:7])

df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
print(df)
melted = pd.melt(df, ['key'])
print(melted)
reshaped = melted.pivot('key', 'variable', 'value')
print(reshaped)
print(reshaped.reset_index())
print(pd.melt(df, id_vars=['key'], value_vars=['A', 'B']))
print(pd.melt(df, value_vars=['A', 'B', 'C']))
print(pd.melt(df, value_vars=['key', 'A', 'B']))
