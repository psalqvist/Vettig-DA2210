import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson

if __name__ == "__main__":
    # get poisson process with average visitors 300 over 100 000 days
    X = pd.Series(poisson.rvs(300, size=100000))
    # count the values, how many times did we have 300 visitors and so on...
    data = X.value_counts().sort_index()
    dict = data.to_dict()
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.xlabel('Visitors per day')
    plt.ylabel('Frequency')
    plt.title('Histogram over visitors per day with average 300, under 100 000 days.')
    ax.bar(list(dict.keys()), list(dict.values()), align='center')
    plt.show()
