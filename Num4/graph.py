import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# Get data from files
data1 = pd.read_csv("results.csv", sep=" ")
x1 = data1['N'].values
y1 = data1['time(N)'].values

plt.figure(figsize=(7, 5))
plt.plot(x1, y1,  label="time")


plt.title('Czas do uzyskania rozwiązania')
plt.legend()
plt.xlabel("N")
plt.ylabel("s")

plt.xlim(1, 50)
plt.xticks((1,10,20,30,40,50))



plt.show()

# plt.plot(x, y)
# plt.show()

