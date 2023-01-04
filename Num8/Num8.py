import numpy as np
import sys

def getDataFromFile(filename: str):
    try:
        with open(filename, "r", encoding='utf-8') as file:
            data = []
            for line in file:
                args = line.rstrip().split(" ")
                args = list(map(float, args))
                data.append(args)
    except FileNotFoundError:
        print("File not found!")
        return []
    except ValueError:
        print(f"{line}")
        return []

    return np.array(data)

def F(x, factors):

    if (len(factors) != 4):
        return None

    return factors[0] * np.sin(2*x) +\
            factors[1] * np.sin(3*x) +\
            factors[2] * np.cos(5*x) +\
            factors[3] * np.exp(-x)

def main():
    if (len(sys.argv) < 2):
        print("Input filename with data in args!")
        sys.exit(1)
    data = getDataFromFile(sys.argv[0])
    print(data)

if __name__ == "__main__":
    main()