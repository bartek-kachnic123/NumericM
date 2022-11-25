import matplotlib.pyplot as plt
import pandas as pd



# Get data from files
data1 = pd.read_csv("gaus-siedel3.csv", sep=" ")
data2 = pd.read_csv("jacobi3.csv", sep=" ")


x1 = data1['k'].values
y1 = data1['E(k)'].values

x2 = data2['k'].values
y2 = data2['E(k)'].values

plt.figure(figsize=(6, 4))
plt.plot(x1, y1,  label="Gauss-Seidla")
plt.plot(x2, y2,  label="Jacobi")
plt.title('Gauss-Seidla vs Jacobi method zestaw 3')
plt.legend()
plt.xlabel("k")
plt.ylabel("E(k)")
plt.xscale("log", base=10)
plt.yscale("log", base=10)
plt.show()

# plt.plot(x, y)
# plt.show()

