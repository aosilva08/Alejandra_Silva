# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#prices of Tesla (TSLA) from January 1st 2019 to December 31st 2021.

#Hint: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-alphavantage
#Hint: https://www.alphavantage.co/support/#api-key

import pandas as pd
import datetime
import requests
import os
from datetime import datetime
import pandas_datareader.data as web

start = datetime(2019, 1,  1)
end   = datetime(year=2021, month=12, day=31)
series = 'TSLA'



df = web.DataReader(series, "av-monthly", start=start,
                     end=end,
                     api_key= 'O0L0XD9N7X43OJ25')

#  Then use Pandas DataReader's interface for Alpha Vantage, not the
#  API that they describe on their site (DataReader does all that for
#  you!)


# 2. Create a new column that holds the rolling 3 month average.

df['av_3m_roll'] = df['close'].rolling(3).mean()


# 3. Create a new dataframe from the base data from part 1 that resamples
# the data to quarterly, using the mean value.


df.index = pd.to_datetime(df.index)
df_q = df.resample('Q').mean()


# 4. Create a figure showing the time series for the monthly level and
# the monthly rolling average together.
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6) ) 
x= pd.to_datetime(df.index)
ax.plot(x, df['close'],'r-', label = 'Mean')
ax.plot(x, df['av_3m_roll'],'b-', label = 'Rolling 3m mean')
ax.leyend(loc= 'upper right')

ax.tick_params(axis="x", labelrotation= 45)
ax.set_tittle('Tesla Monthly Average closing Stock Price')



