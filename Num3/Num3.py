import numpy as np
import sys


def makeArrayA(N):

    arrayA = np.zeros((4, N))

    for i in range(0, N):
        arrayA[0, i] = 0.4 / pow(i+1, 2)  # first row
        arrayA[1, i] = 0.1 / (i+1)         # second row
        arrayA[2, i] = 1.2             # third row
        arrayA[3, i] = 0.2             # fourth row

    return arrayA


def main():
    if len(sys.argv) != 2:
        print("Wrong num of args!")
        exit(1)
    N = int(sys.argv[1])  # length of array
    x = np.arange(1, 101)  # 1 to 100
    print(x)

    A = makeArrayA(N)
    print(A)


if __name__ == "__main__":
    main()
