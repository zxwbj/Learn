import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('movies_metadata.csv')

# print(df.head())
# print(df.columns)
# print(df.info())
# print(df.iloc[2])
# print(df.iloc[[2]])
# print(df.shape)
# print(df.title)
# print(df.genres)
# print(df[['title', 'genres']])
# print(df[df.title == 'Grumpier Old Men'])
# # df = df.set_index('title')
# # print(df.loc['Grumpier Old Men'])
#
# small_df = df[['title', 'release_date', 'budget', 'revenue', 'runtime', 'vote_count']]
# print(small_df.head())
#
# print(df.head(10))
#
# print(small_df.sort_values(by='release_date'))
# print(small_df[small_df.release_date > '1995-11-01'])
# print(small_df.sort_values(by='runtime', ascending=False))
# print(small_df[(small_df.revenue > 2000000) & (small_df.budget < 1000000)])
# print(small_df.runtime.max())
# print(small_df.runtime.min())
#
# print(small_df.vote_count.quantile(0.7))
# print(small_df[small_df.vote_count > 500])

df.sort_values(by='vote_count', inplace=True, ascending=False)
plt.bar(df.title, df.vote_count, color='orange')
plt.xlabel('movie')
plt.ylabel('vote count')
plt.title('vote count of movie', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.legend(['vote count'])
plt.show()

