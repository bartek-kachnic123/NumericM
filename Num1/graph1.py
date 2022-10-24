import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def annot_min(x,y,corx,cory, ax=None):
    xmin = x[np.argmin(y)]
    ymin = y.min()
    text= "h={}, E(h)={}".format(xmin, ymin)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmin, ymin), xytext=(corx,cory), **kw)

def check_deritive_error(h, E, x=0.2):
    num = np.fabs(-np.sin(x) / 2 ) - (2*E * np.fabs(np.sin(x)) / h * h)
    print(f'check is {num}')

# Get data from files
data1 = pd.read_csv("resultsA_f.csv", sep=";")
data2 = pd.read_csv("resultsA_d.csv", sep=";")


x1 = data1['h'].values
y1 = data1['E(h)'].values

x2 = data2['h'].values
y2 = data2['E(h)'].values

minF = min(zip(x1, y1), key = lambda t: t[1]) # finding lowest y in pairs (x, y)
minD = min(zip(x2, y2), key = lambda t: t[1]) # finding lowest y in pairs (x, y)

print(minF)
print(min(y1))
plt.plot(x1, y1,  label="float")
annot_min(x1, y1, 0.90, 0.12)
annot_min(x2,y2, 0.50, 0.03)
check_deritive_error(minF[0], minF[1])
plt.plot(x2, y2,  label="double")
plt.title('Dh = (sin(x+h) - sin(x)) / h')
plt.legend()
plt.xlabel("h")
plt.ylabel("E(h)")
plt.xscale("log", base=10)
plt.yscale("log", base=10)
plt.show()

# plt.plot(x, y)
# plt.show()

