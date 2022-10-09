import matplotlib.pyplot as plt
import pandas as pd


data1 = pd.read_csv("results.csv", sep=";")
data2 = pd.read_csv("results1_d.csv", sep=";")


x1 = data1['h'].values
y1 = data1['E(h)'].values

x2 = data2['h'].values
y2 = data2['E(h)'].values

plt.plot(x1, y1, label="float")
plt.plot(x2, y2,  label="double")
plt.legend()
plt.xlabel("h")
plt.ylabel("E(h)")
plt.xscale("log", base=10)
plt.yscale("log", base=10)
plt.show()

# plt.plot(x, y)
# plt.show()