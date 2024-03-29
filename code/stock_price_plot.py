import pandas as pd
import matplotlib.pyplot as plt

stock_price = pd.read_csv('../sample_data/intel.csv', parse_dates= True, index_col='Date')

stock_price.loc['2017-10-16':'2017-10-20',['Open','Close']].plot(style='.-', title='Intel')

plt.show()
