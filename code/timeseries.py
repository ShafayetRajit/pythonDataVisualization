import pandas as pd

sales_data = pd.read_csv('../sample_data/sales_data.csv', parse_dates=True, index_col='InvoiceDate')

#print(sales_data.info()) #columns, data types, count

#morning_sale = sales_data.loc['2010-12-01 08:00:00':'2010-12-01 09:00:00'] #timeframe begin:end
#print(morning_sale)

dates = ['12-01-2010 08:26','12-02-2010 16:38','12-03-2010 12:24','12-05-2010 10:03','12-05-2010 10:03']
time_format = '%d-%m-%Y %H:%M'

new_time = pd.to_datetime(dates, format = time_format) #converting to a new format

#print(new_time)

daily_sale = sales_data.loc['2010-12-01']

weekly = sales_data.loc[:,'Quantity'].resample('Y').sum() #resample D W Y

sale = sales_data['Quantity']['2010-12-01']

quantity = sale.resample('H').min() #finds min by hour in a day

search = sales_data['Description'].str.contains('POPPY') #search poppy in desc
poppy_sale = search.resample('W').sum()

print(poppy_sale)
