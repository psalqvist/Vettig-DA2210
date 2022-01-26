import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
l = []

with open('rnorm4.txt', 'r') as f:
     for i in f:
        l.append(float(i))

f= np.loadtxt('rnorm4.txt', unpack='False')

# set bins' interval for your data
# You have following intervals: 
# 1st col is number of data elements in [0,10000);
# 2nd col is number of data elements in [10000, 20000); 
# ...
# last col is number of data elements in [100000, 200000]; 
bins = range(0, int(max(l)), 10)

plt.hist(f, histtype='bar', bins = bins)
plt.xlabel('Diameter')
plt.ylabel('Number of Chondrules')
plt.title('Distribution of chondules diameter')
plt.legend()
plt.show()