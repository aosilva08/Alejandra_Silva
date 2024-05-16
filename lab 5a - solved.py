#NAMES

import pandas as pd

#1. It's a puzzle! Load these three dataframes and explore their structure.
#Then combine them so that the result is a single dataframe with the columns 
#"date", "place", "value1", "value2", with the date columns being datetime 
#objects that run from 1/2020 to 10/2021, without modifying any starter code.

data1 = {'date':['2020-1-1', '2020-4-1', '2020-7-1', '2020-10-1'],
         'place1':[39, 17, 20, 88],
         'place2':[55, 88, 19, 42]}

data2 = {'date':['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01',
                 '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01'],
         'place1':[1, 4, 7, 2, 5, 8, 11, 13],
         'place2':[2, 5, 8, 6, 6, 9, 13, 15]}

data3 = {'date':['2021-1-1', '2021-4-1', '2021-7-1', '2021-10-1']*2,
         'place':['place1']*4 + ['place2']*4,
         'value1':[33, 43, 53, 34, 35, 46, 47, 48]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

df1 =df1.melt(id_vars='date', value_vars=None, var_name='place', value_name='value1')
df2 =df2.melt(id_vars='date', value_vars=None, var_name='place', value_name='value2')


df3

df_vf = pd.concat([df1, df3])
df_vf

df_vf['date'] = pd.to_datetime(df_vf['date'])
df2['date'] = pd.to_datetime(df2['date'])


df_merged = df_vf.merge(df2, on= ['date', 'place'], how='outer', indicator=True)
df_merged


#2. You had to do some merging in part 1. If you did not already, go back and use
#some assert statements to verify that the dataframes did what you expected.

start_len = len(df_vf)

fin_len = len(df_merged)

assert(start_len == fin_len), 'unexpected expansion'

#3. Is the dataframe from part 1 in long or wide format? Write code to convert it
#into the other.

# is long 

df_merged

df_wide = df_merged.pivot(index='date', columns='place', values=['value1','value2'])
df_wide