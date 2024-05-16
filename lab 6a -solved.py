#NAMES

import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present.  Create a line plot, with vertical
# lines to mark recessions:
#   March 2001 - November 2001
#   December 2007 - June 2009
#   February 2020 - April 2020
# Next continue to clean up the figure, adding a title, axis labels, shading the area
# that designates recessions, and any other changes that come to mind. If you manually
# copy-pasted the code for each recession line, try instead to put them in containers
# and use a for-loop.

df = pd.read_csv('unrate.csv', parse_dates=['DATE'])
recessions = [
    ('2001-03-01', '2001-11-30'),
    ('2007-12-01', '2009-06-30'),
    ('2020-02-01', '2020-04-30')
]


fig, ax = plt.subplots()
ax.plot(df['DATE'], df['UNRATE'], label ='Unemployment Rate')
ax.set_title('US Unemployment Rate with Recessions')
ax.set_xlabel('Year')
ax.set_ylabel('Unemployment Rate (%)')
ax.legend(loc= 'upper left') 
    
for start, end in recessions:
    ax.axvspan(pd.to_datetime(start), pd.to_datetime(end), color='grey', alpha=0.5)




