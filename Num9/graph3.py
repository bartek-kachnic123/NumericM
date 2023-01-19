import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# Get data from files
data4 = pd.read_csv("newton2.csv", sep=";")
x4 = data4['n'].values
y4 = data4['|x-x*|'].values

plt.figure(figsize=(7, 5))


plt.plot(x4, y4,  label="Newton")

plt.xscale('log')
plt.yscale('log')

plt.title('n = 2')
plt.legend()
plt.xlabel("k iteration")
plt.ylabel("|x-x*|")

plt.show()