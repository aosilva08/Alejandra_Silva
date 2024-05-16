#NAMES: ALEJANDRA SILVA

#For the following questions, load the iris.csv dataset into a Pandas
#DataFrame. Make sure you set up an absolute path as described in 
#lecture, and if you're working with others, you should each update
#it to work on your computer.

#1. Explore the data.  How many categories of flowers are there? What
#   are the mean and median values, and the standard deviation?  How 
#   would you find the mean values per type of flower?  Right now you
#   can implement this with subsetting; next week we will cover how to
#   do this using groupby.
import pandas as pd

import os
os.getcwd()

base_path = r'c:\users\aosil\downloads'
path = os.path.join(base_path, 'iris.csv')
path 

iris_df = pd.read_csv(path)

iris_df

iris_df.head()
iris_df.tail()
iris_df.shape

iris_df.info()
iris_df.groupby(iris_df.species).mean()


#2. Locate the max value across all four measures.  Use loc to display
#   just the rows that contain those values.
max_values = iris_df.max() 

for col in max_values.index:
    display(iris_df[iris_df[col] == max_values[col]])

#3. How many of observations for each species of iris is in the data?

species_counts = iris_df['species'].value_counts()
print(species_counts)

#4. Using one line of code, divide each value by the mean for that measure,
#   and assign the result to four new columns.  How is this different from 
#   a zscore?  How would you make this a zscore instead?  What's the problem
#   with doing this without accounting for the values in the species column?


for col in iris_df.columns[:-1]:  # excluding the species column
    iris_df[col + '_norm_by_mean'] = iris_df[col] / iris_df[col].mean()

print(iris_df.head())

for col in iris_df.columns[:-5]:  # only original numeric columns
    iris_df[col + '_zscore'] = (iris_df[col] - iris_df[col].mean()) / iris_df[col].std()

print(iris_df.head())

# Discussion:
# Normalizing by mean scales data by the mean of each feature, which is not a standard normalization technique.
# Z-score (Standard Score) normalization scales data with both mean and standard deviation, making the mean of
# the data 0 and the standard deviation 1. This is useful for comparison across different scales of data.



#5. Create a new column named "petal_area" which is equal to the length
#   times the width.  Note that this isn't really the area of the petal, since
#   petals presumably aren't rectangles.

iris_df['petal_area'] = iris_df['petal_length'] * iris_df['petal_width']
print(iris_df.head())


#6. Subset the data to a new variable that is a dataframe with only virginica 
#   flowers.  Now add a new column to this subset that is equal to 1 if the 
#   sepal_length is greater than the mean sepal_length, else 0.  Did you get a
#   SettingWithCopyWarning message?  Modify your copying to do away with the 
#   warning.  Hint: You can create this with apply, or with map if you also
#   create a global variable holding the mean.

for col in max_values.index:
    display(iris_df[iris_df[col] == max_values[col]])