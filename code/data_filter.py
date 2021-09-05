import pandas as pd
import matplotlib.pyplot as plt

app_data = pd.read_csv('../sample_data/googleplaystore.csv') #read file

print(app_data)

print(app_data[app_data['Rating'] >= 4.9]) #conditional

print(app_data[(app_data['Genres']=='Education') & (app_data['Rating'] >= 4.9)]) #combining conditions
