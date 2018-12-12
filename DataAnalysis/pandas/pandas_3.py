import numpy as np
import pandas as pd


# df = pd.read_csv('examples/ex1.csv')
# print(df)
# df = pd.read_table('examples/ex1.csv', sep=',')
# print(df)
# df = pd.read_csv('examples/ex2.csv', header=None)
# print(df)
# df = pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
# print(df)

# names = ['a', 'b', 'c', 'd', 'message']
# print(pd.read_csv('examples/ex2.csv', names=names, index_col='message'))
#
# parsed = pd.read_csv('examples/csv_mindex.csv', index_col=['key1', 'key2'])
# print(parsed)

# result = pd.read_table('examples/ex3.txt', sep='\s+')
# # print(result)
# #
# # df = pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3])
# # print(df)

# result = pd.read_csv('examples/ex5.csv')
# print(result)
# # print(result.isnull())
# # print(pd.isnull(result))
#
# result = pd.read_csv('examples/ex5.csv', na_values=['NULL'])
# print(result)
#
# sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
# print(pd.read_csv('examples/ex5.csv', na_values=sentinels))
#
# print(pd.options.display.max_rows)
# pd.options.display.max_rows = 10
# result = pd.read_csv('examples/ex6.csv')
# print(result)
#
# result = pd.read_csv('examples/ex6.csv', nrows=5)
# print(result)

# print(pd.options.display.max_rows)
pd.options.display.max_rows = 10
chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
print(chunker)
# for piece in chunker:
#     print(piece)

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot[:10])
