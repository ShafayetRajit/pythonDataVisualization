import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../sample_data/intel.csv', index_col = 'Date', parse_dates = True)

#print(df.head())


df['Close'].plot() #plotting value of a specific column 
plt.axis(('10-10-17', '24-04-18', 30, 60)) #defining axis
plt.title('Stock Price') #title of plot
plt.show()
plt.savefig('stockprice.pdf') #saving plot as pdf
