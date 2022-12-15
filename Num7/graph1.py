import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Get data from files
data1 = pd.read_csv("a1.csv", sep=";")
data2 = pd.read_csv("a2.csv", sep=";")
data3 = pd.read_csv("a3.csv", sep=";")
data4 = pd.read_csv("a4.csv", sep=";")

xlabel = "N"
ylabel = "W(N)"

x1 = data1[xlabel].values
y1 = data1[ylabel].values

x2 = data2[xlabel].values
y2 = data2[ylabel].values

x3 = data3[xlabel].values
y3 = data3[ylabel].values

x4 = data4[xlabel].values
y4 = data4[ylabel].values



plt.plot(x1, y1,  label=F"N={len(x1)-1}")
plt.plot(x2, y2,  label=F"N={len(x2)-1}")
plt.plot(x3, y3,  label=F"N={len(x3)-1}")
plt.plot(x4, y4,  label=F"N={len(x4)-1}")
plt.title('Jednorodne węzły interpolacji')
plt.legend()
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.xscale("log", base=10)
plt.yscale("log", base=10)
plt.show()

# plt.plot(x, y)
# plt.show()

