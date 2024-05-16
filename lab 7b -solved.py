import pandas as pd
import pandas_datareader.data as web
import statsmodels.api as sm
import matplotlib.pyplot as plt

series = {'CPMNACSCAB1GQDE':'GDPGermany',
          'LRUNTTTTDEQ156S':'EMPGermany',
          'CPMNACSCAB1GQPL':'GDPPoland',
          'LRUNTTTTPLQ156S':'EMPPoland'}
df = web.DataReader(series.keys(), 'fred', start='1995-01-01', end='2019-10-01')

df = df.rename(series, axis=1)


# 1)
# This data is from lecture 18.  Explore it using plots and summary
# statistics. What is wrong with the employment data from Poland? 
# Then, apply an HP filter from the statsmodels library, and filter 
# all four series.  Plot the cycles, trends, and original values to
# see what is happening when you filter.

df = df.reset_index()

df_long = pd.wide_to_long(df, ['GDP', 'EMP'], i='DATE',
                                              j='COUNTRY',
                                              suffix='\\w+')

fig, ax = plt.subplots()
for label, d in df_long.reset_index().groupby('COUNTRY'):
    d.plot(x='DATE', y='GDP', label=label, ax=ax)
ax.legend()
ax.set_title('GDP')

fig, ax = plt.subplots()
for label, d in df_long.reset_index().groupby('COUNTRY'):
    d.plot(x='DATE', y='EMP', label=label, ax=ax)
ax.legend()
ax.set_title('EMP')

#hp

df['EMPPoland'].isna().sum()
df['EMPPoland'] = df['EMPPoland'].interpolate(method= 'linear')

g_cycle_GDP, g_trend_GDP = sm.tsa.filters.hpfilter(df['GDPGermany'], lamb=1600)
p_cycle_GDP, p_trend_GDP = sm.tsa.filters.hpfilter(df['GDPPoland'], lamb=1600)

fig, axs = plt.subplots(2, 1, figsize=(12,6))
axs[0].plot(g_cycle_GDP.index, g_cycle_GDP, 'b-', label='GDP Germany')
axs[0].plot(g_cycle_GDP.index, p_cycle_GDP, 'r-', label='GDP Poland')
axs[1].plot(g_trend_GDP.index, g_trend_GDP, 'b-')
axs[1].plot(g_trend_GDP.index, p_trend_GDP, 'r-')
axs[0].set_ylabel('Cycle')
axs[1].set_ylabel('Trend')
fig.legend(loc='upper center', ncols=2)
plt.show()

g_cycle_EMP, g_trend_EMP = sm.tsa.filters.hpfilter(df['EMPGermany'], lamb=1600)
p_cycle_EMP, p_trend_EMP = sm.tsa.filters.hpfilter(df['EMPPoland'], lamb=1600)

fig, axs = plt.subplots(2, 1, figsize=(12,6))
axs[0].plot(g_cycle_EMP.index, g_cycle_EMP, 'b-', label='EMP Germany')
axs[0].plot(g_cycle_EMP.index, p_cycle_EMP, 'r-', label='EMP Poland')
axs[1].plot(g_trend_EMP.index, g_trend_EMP, 'b-')
axs[1].plot(g_trend_EMP.index, p_trend_EMP, 'r-')
axs[0].set_ylabel('Cycle')
axs[1].set_ylabel('Trend')
fig.legend(loc='upper center', ncols=2)
plt.show()



# 2)
# The code from the lecture includes a function that implements the
# Hamilton filter, though we did not go over the code in detail.
# Copy that function over and try to understand most of what it is
# doing (you may have to test it in pieces) and then apply it to
# this data. Modify your plots from question 1 to compare the results
# of the Hamilton and HP filters to the unfiltered values.

import numpy as np

def hamilton_filter(data, h=8, p=4):
    def _shift(orig_series, n):
        #implements efficient (positive) shifting for non-Series dtypes
        new_series = np.empty_like(orig_series)
        new_series[:n] = np.NaN
        new_series[n:] = orig_series[:-n]
        return new_series

    new_cols = [_shift(data, s) for s in range(h, h+p)]

    exog = sm.add_constant(np.array(new_cols).transpose())
    model = sm.GLM(endog=data, exog=exog, missing='drop')
    res = model.fit()

    trend = res.fittedvalues
    rand = data - _shift(data, h)
    cycle = res.resid_pearson
    return cycle, trend, rand

g_cycle, g_trend, _ = hamilton_filter(df['GDPGermany'])
p_cycle, p_trend, _ = hamilton_filter(df['GDPPoland'])

fig, axs = plt.subplots(2, 1, figsize=(12,6))
axs[0].plot(g_cycle.index, g_cycle, 'b-', label='GDP Germany')
axs[0].plot(g_cycle.index, p_cycle, 'r-', label='GDP Poland')
axs[1].plot(g_trend.index, g_trend, 'b-')
axs[1].plot(g_trend.index, p_trend, 'r-')
axs[0].set_ylabel('Cycle')
axs[1].set_ylabel('Trend')
fig.legend(loc='upper center', ncols=2)
plt.show()

g_cycle.name = 'Germany_hamilton'
p_cycle.name = 'Poland_hamilton'

model = sm.OLS(g_cycle, sm.add_constant(p_cycle))
result = model.fit()
result.summary()


g_cycle_EMP, g_trend_EMP, _ = hamilton_filter(df['EMPGermany'])
p_cycle_EMP, p_trend_EMP, _ = hamilton_filter(df['EMPPoland'])

fig, axs = plt.subplots(2, 1, figsize=(12,6))
axs[0].plot(g_cycle_EMP.index, g_cycle_EMP, 'b-', label='EMP Germany')
axs[0].plot(g_cycle_EMP.index, p_cycle_EMP, 'r-', label='EMP Poland')
axs[1].plot(g_trend_EMP.index, g_trend_EMP, 'b-')
axs[1].plot(g_trend_EMP.index, p_trend_EMP, 'r-')
axs[0].set_ylabel('Cycle')
axs[1].set_ylabel('Trend')
fig.legend(loc='upper center', ncols=2)
plt.show()

g_cycle_EMP.name = 'EMP_Germany_hamilton'
p_cycle_EMP.name = 'EMP_Poland_hamilton'

model = sm.OLS(g_cycle_EMP, sm.add_constant(p_cycle_EMP))
result = model.fit()
result.summary()
