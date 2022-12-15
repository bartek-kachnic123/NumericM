import numpy as np

def y(x):
    return 1 / (1 + 25 * np.power(x, 2))

def first_interpolation(n, filename):
    file = open(filename, "w", encoding='utf-8')
    file.write("N;W(N)\n")
    for i in range(n+1): # from 0 to n
        x = -1 + (2 * (i / (n + 1)))
        result = y(x)
        file.write(f'{i};{result}\n')

    file.close()

def second_interpolation(n, filename):
    file = open(filename, "w", encoding='utf-8')
    file.write("N;W(N)\n")
    for i in range(n+1): # from 0 to n
        x = np.cos((2*i + 1) / (2 * (n + 1)))
        result = y(x)
        file.write(f'{i};{result}\n')

    file.close()

def main():
    nSets = (5, 10, 25, 50)
    filenamesA = (f'a{i}.csv' for i in range(1, 5))
    filenamesB = (f'b{i}.csv' for i in range(1, 5))

    dataA = tuple(zip(nSets, filenamesA))
    dataB = tuple(zip(nSets, filenamesB))

    for i in range(len(nSets)):
        first_interpolation(dataA[i][0], dataA[i][1])
        second_interpolation(dataB[i][0], dataB[i][1])
        
    print("Wyniki zapisano do plików!")
if __name__ == "__main__":
    main()