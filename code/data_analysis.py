import pandas as pd
import matplotlib.pyplot as plt

stock = pd.read_csv('../sample_data/tesla.csv') #open file

print(stock.describe()) #prints count, mean, std, 25/50/75%, max

print(stock['Close'].mean()) #mean of a specific column
print(stock['Close'].min()) #min of a specific column
print(stock['Close'].max()) #max of a specific column

stock['Close'].plot(kind = 'box') #boxplot of close values 
plt.show()
