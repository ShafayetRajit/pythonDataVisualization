import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('intel.csv', index_col = 'Date', parse_dates = True)

#print(df.head())


df['Close'].plot()
plt.axis(('10-10-17', '24-04-18', 30, 60))
plt.title('Stock Price')
plt.show()
plt.savefig('stockprice.pdf')
