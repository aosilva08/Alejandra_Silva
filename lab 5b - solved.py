#NAMES: ALEJANDRA SILVA

import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

# 1) Create a groupby object using "clarity" and "color" as the keys

df1 = df.groupby(['clarity','color'])

df1.groups


# 2) Display the describe() output JUST for group color=E, clarity=SI2

df1.get_group(('SI2','E')).describe()


# 3) Display the max value for price in each group

df1.apply(lambda g: g['price'].max())

# 4) Display the min value for price in each group

df1.apply(lambda g: g['price'].min())


# 5) Write four different functions:
#    - one that works with map on the values in a column

df['depth>60ct'] = df['depth'].map(lambda c: 1 if c > 60 else 0)

#    - one that works with apply on the values in a row

df['carat_price'] = df.apply(lambda r: r['carat'] * r['price'], axis=1)

#    - one that works with apply on the values in a column

df['price_in_soles'] = df['price'].apply(lambda price: price * 3.7)

#    - one that works with apply on a groupby object

df2 = df.groupby(['cut', 'color']).apply(lambda g: (g['price'] / g['carat']).mean())

# 6) Display only the maximum price for each clarity.

df.groupby('clarity').max(['price'])['price']

df.groupby('clarity')['price'].max()


# 7) Stretch goal! Which clarity of diamond has the diamond that is
#    the largest outlier in size (carats) from the mean for that group?

mean_carats = df.groupby('clarity')['carat'].mean()
df['mean_carat'] = df['clarity'].map(mean_carats)

df['diff_from_mean'] = (df['carat'] - df['mean_carat']).abs()

max_outliers = df[df['diff_from_mean'] == df['diff_from_mean'].max()]['clarity']

