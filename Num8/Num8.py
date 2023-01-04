import numpy as np
import matplotlib.pyplot as plt
import sys


def getDataFromFile(filename: str):
    try:
        with open(filename, "r", encoding='utf-8') as file:
            x = []
            y = []
            for line in file:
                args = line.rstrip().split(" ")
                args = list(map(float, args))
                x.append(args[0])
                y.append(args[1])
    except FileNotFoundError:
        print("File not found!")
        return []
    except ValueError:
        print(f"{line}")
        return []

    return x, y


def F(x, factors):

    if (len(factors) != 4):
        return None

    return factors[0] * np.sin(2*x) +\
        factors[1] * np.sin(3*x) +\
        factors[2] * np.cos(5*x) +\
        factors[3] * np.exp(-x)


def solve_A(filename: str):
    x, y = getDataFromFile(filename)

    A = []
    for i in range(len(x)):
        A.append([np.sin(2*x[i]), np.sin(3*x[i]),
                  np.cos(5*x[i]), np.exp(-x[i])])

    A = np.array(A)
    factors = np.linalg.solve(A.T @ A, A.T @ y)
    print("Factors: ", factors)

    return factors


def make_GraphA(filename, factors):
    x, y = getDataFromFile(filename)

    yResults = []
    for i in range(len(x)):
        yResults.append(F(x[i], factors))
    plt.figure(figsize=(7, 5))
    plt.scatter(x, y, color="red")
    plt.plot(x, yResults, label="F(x)")
    plt.title("Metoda najmniejszych kwadratów")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def G(x, factors):
    return factors[0] - factors[1] * x +\
        factors[2] * np.power(x, 2) +\
        factors[3] * np.sin(np.power(x, 3))


def solve_B():
    myFactors = [0.125, 10, 0.875, 2.125]

    x = []
    y = []
    for i in range(100):
        x.append(i/10)
        y.append(G(x[i], myFactors) + np.random.random())

    A = []
    for i in range(len(x)):
        A.append([1, -x[i], np.power(x[i], 2), np.sin(np.power(x[i], 3))])

    A = np.array(A)
    factors = np.linalg.solve(A.T @ A, A.T @ y)
    print("Old factors: ", myFactors)
    print("New factors: ", factors)
    return x, y, factors


def make_GraphB(xData, yData, factors):

    yResults = []
    for i in range(len(xData)):
        yResults.append(G(xData[i], factors))

    plt.figure(figsize=(7, 5))
    plt.scatter(xData, yData, color="red")
    plt.plot(xData, yResults, label="G(x)")
    plt.title("Metoda najmniejszych kwadratów")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def main():
    if (len(sys.argv) < 2):
        print("Input filename with data in args!")
        sys.exit(1)

    factors = solve_A(sys.argv[1])

    x, y, factors2 = solve_B()

    #make_GraphA(sys.argv[1], factors)
    make_GraphB(x, y, factors2)


if __name__ == "__main__":
    main()
