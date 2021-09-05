import pandas as pd
import matplotlib.pyplot as plt

expec = pd.read_csv('../sample_data/irish_life_expec.csv')

expec.plot(kind = 'bar', x = 'year', y = 'life expec', color='g', legend = True)
expec.plot(kind = 'scatter', x = 'year', y = 'life expec') #scatter plot



plt.title('Life expectancy')

plt.show()
