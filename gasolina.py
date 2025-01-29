
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('gasolina.csv')

data

plt.plot (data[ 'dia'], data['venda'])
plt.show()
plt.savefig('gasolina.png')
