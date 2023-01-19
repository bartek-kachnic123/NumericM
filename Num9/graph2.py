import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# Get data from files
data1 = pd.read_csv("bisection3.csv", sep=";")
x1 = data1['n'].values
y1 = data1['|x-x*|'].values

data2 = pd.read_csv("falsi3.csv", sep=";")
x2 = data2['n'].values
y2 = data2['|x-x*|'].values

data3 = pd.read_csv("secant3.csv", sep=";")
x3 = data3['n'].values
y3 = data3['|x-x*|'].values

data4 = pd.read_csv("newton3.csv", sep=";")
x4 = data4['n'].values
y4 = data4['|x-x*|'].values

plt.figure(figsize=(7, 5))

plt.plot(x1, y1,  label="bisection")
plt.plot(x2, y2,  label="falsi")
plt.plot(x3, y3,  label="secant")
plt.plot(x4, y4,  label="Newton")

plt.xscale('log')
plt.yscale('log')

plt.title('n = 3')
plt.legend()
plt.xlabel("k iteration")
plt.ylabel("|x-x*|")

plt.show()