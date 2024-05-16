#NAMES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='petal_length',
                data=df, hue='species')
plt.show()

#Recreate this plot in Matplotlib, without using Seaborn!
#Then try adding some of your own customizations to the 
#plot using MatPlotLib methods

df_g = df.groupby('species')



fig, ax = plt.subplots()
ax.scatter(df_g.get_group('setosa')['sepal_length'], df_g.get_group('setosa')['petal_length'], label='setosa')
ax.scatter(df_g.get_group('versicolor')['sepal_length'], df_g.get_group('versicolor')['petal_length'], label='versicolor')
ax.scatter(df_g.get_group('virginica')['sepal_length'], df_g.get_group('virginica')['petal_length'], label='virginica')
ax.legend(loc='upper left', title = 'species')

for species, groups in df_g:
    plt.scatter(groups['sepal_length'],groups['petal_length'], label = species)
    plt.legend(loc='upper left', title = 'species')
    


