import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.formula.api import ols

file = open('billionaires.csv', 'r')

mydat = []

for i in file:
    mydat.append(i)

print(mydat[:3])
file.close()

# load file in dataframe
df = pd.read_csv("billionaires.csv")
df.head(3)

log_score = np.log(df[['rank']])

fig = df.plot.line('rank', 'wealth.worth in billions').get_figure()
fig.savefig('test.pdf')
