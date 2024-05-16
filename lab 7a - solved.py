#NAMES

import pandas as pd
import numpy as np 
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression 

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'
df = pd.read_csv(url_to_csv)


# 1) Explore the data & produce some basic summary stats  

df.describe()

# 2) Run a regression of price (y) on carat (x), including an 
#    intercept term.  Report the estimates of the intercept & slope 
#    coefficients using each of the following methods:
#        a) NumPy

y = df['price'].to_numpy()
x = df[['carat']].to_numpy()

m, b = np.polyfit(x, y , deg=1)
gen_lin1d = np.poly1d((m,b))

print(m, b)


#        b) statsmodels (smf) 

model = smf.ols('price ~ carat', data= df)
result = model.fit()
print(result.params)



#        c) statsmodels (sm)

df = sm.add_constant(df)
model = sm.OLS(endog= df['price'], exog = df[['const', 'carat']])
result = model.fit()

print(result.params)

#        d) scikit-learn (LinearRegression)  
x = df[['carat']].shape
y = df[['price']].shape

model = LinearRegression(fit_intercept=True)
result = model.fit(x,y)
print(result.intercept_)
print(result.coef_)



#           Hint:  scikit-learn only works with array-like objects.    
#    Confirm that all four methods produce the same estimates.



# 3) Run a regression of price (y) on carat, the natual logarithm of depth  
#    (log(depth)), and a quadratic polynomial of table (i.e., include table & 
#    table**2 as regressors).  Estimate the model parameters using any Python
#    method you choose, and display the estimates.  

model_3 = smf.ols('price ~ carat + np.log(depth) + table + I(table**2)', data= df)
result_3 = model_3.fit()
print(result_3.params)

# 4) Run a regression of price (y) on carat and cut.  Estimate the model 
#    parameters using any Python method you choose, and display the estimates.  

model_4 = smf.ols('price ~ carat + C(cut)', data= df)
result_4 = model_4.fit()
print(result_4.params)

# 5) Run a regression of price (y) on whatever predictors (and functions of 
#    those predictors you want).  Try to find the specification with the best
#    fit (as measured by the largest R-squared).  Note that this type of data
#    mining is econometric blasphemy, but is the foundation of machine
#    learning.  Fit the model using any Python method you choose, and display 
#    only the R-squared from each model.  We'll see who can come up with the 
#    best fit by the end of lab.  

model_5 = smf.ols('price ~ carat + C(cut) + C(color) + C(clarity) + np.log(depth) + np.log(table) ', data= df)
result_5 = model_5.fit()
print(result_5.rsquared)
