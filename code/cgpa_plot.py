import pandas as pd
import matplotlib.pyplot as plt

cgpa = pd.read_csv('../sample_data/cgpa.csv', index_col='semester')

cgpa.plot(y=['CGPA','CS CGPA'], style='.-', title='Completely RANDOM CGPA') #can also be done using .loc, then must provide timeframe
plt.ylabel('CGPA')
plt.show()
