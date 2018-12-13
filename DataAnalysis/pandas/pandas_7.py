import numpy as np
import pandas as pd

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)
print(string_data.isnull())
string_data[0] = None
print(string_data.isnull())

from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())
print(data[data.notnull()])

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
print(data)
print(data.dropna())
print(data.dropna(how='all'))
data[4] = NA
print(data)
print(data.dropna(axis=1))
print(data.dropna(axis=1, how='all'))

df = pd.DataFrame(np.random.randn(7, 3))
print(df)
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))
print(df.fillna(0))
print(df.fillna({1: 3, 2: 0}))
print(df)
df.fillna(0, inplace=True)
print(df)

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=2))

data = pd.Series([1., NA, 3.5, NA, 7])
print(data.fillna(data.mean()))

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
print(data.duplicated())
print(data.drop_duplicates())

data['v1'] = range(7)
print(data)
print(data.drop_duplicates(['k1']))
print(data.drop_duplicates(['k1', 'k2'], keep='last'))

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}
lowercased = data['food'].str.lower()
print(lowercased)
data['animal'] = lowercased.map(meat_to_animal)
print(data)
print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)
print(data.replace(-999, np.nan))
print(data.replace([-999, -1000], [np.nan, 0]))
print(data.replace({-999: np.nan, -1000: 0}))

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
transform = lambda x: x[:4].upper()
print(data.index.map(transform))
print(data)
data.index = data.index.map(transform)
print(data)
print(data.rename(index=str.title, columns=str.upper))
print(data)

print(data.rename(index={'OHIO': 'INDIANA'},columns={'three': 'peekaboo'}))
data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
print(data)

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
print(pd.value_counts(cats))

data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())
col = data[2]
# print(col)
print(col[np.abs(col) > 2])
print(data[(np.abs(data) > 3).any(1)])
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())
print(np.sign(data).head())
print('-------------------------------------------')
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
print(df)
print(sampler)
print(df.take(sampler))
print(df.sample(n=3))

choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)
print(draws)

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
print(pd.get_dummies(df['key']))
print(df['key'])

dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)

