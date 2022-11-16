import numpy as np
import sys
from functools import reduce


def makeArrayA(N):

    arrayA = np.zeros((4, N))

    for i in range(0, N):
        arrayA[0, i] = 0.4 / pow(i+1, 2)  # first row
        arrayA[1, i] = 0.1 / (i+1)         # second row
        arrayA[2, i] = 1.2             # third row
        arrayA[3, i] = 0.2             # fourth row

    return arrayA

def LU_method(arrayA, N):

    for i in range(1, N):
        arrayA[3, i-1] = arrayA[3, i-1] / arrayA[2, i-1] # czesc dolna
        arrayA[2, i] = arrayA[2, i] - (arrayA[1, i-1] * arrayA[3, i-1]) # glowna przekatna U
        arrayA[1, i] = arrayA[1, i] - (arrayA[3, i-1] * arrayA[0, i-1]) # pasek wyzej nad glowna przekatna U
        # array[0, i] // drugi pasek wyzej od glownej przekatnej U bez zmian

    return arrayA

def LU_det(LU):
    return reduce(lambda x, y: x*y, LU[2])

def solveLU(LU, x, N):
    z = np.zeros(N)

    # Forward Substition
    z[0] = x[0]
    for i in range(1, N):
        z[i] = x[i] - (LU[3, i-1] * z[i-1])

    # Back Substition
    b = np.zeros(N)
    b[N-1] = z[N-1] / LU[2, N-1] # last
    b[N-2] = (z[N-2] - (LU[1, N-2] * b[N-1]))/ LU[2, N-2] # prelast
    for i in range(N-3, -1, -1): # From N-3 to 0
        b[i] = (z[i] - (LU[1, i] * b[i+1]) - (LU[0, i] * b[i+2])) / LU[2, i]

    return b


def main():
    N = 0
    if len(sys.argv) != 2:
        N = 100
    else: N = int(sys.argv[1]) 

    x = np.arange(1, N+1)  # 1 to 100

    A = makeArrayA(N)
    A = LU_method(A, N)
    print("Wyznacznik macierzy A wynosi: ", LU_det(A))
    print("Rozwiazanie macierzy Ay = x:")
    print(solveLU(A, x, N))




if __name__ == "__main__":
    main()
