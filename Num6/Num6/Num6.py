import numpy as np

def matrixFromFile(filename, separator=' '):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            matrix = []
            lines = file.readlines()
            
            if len(list(lines)) == 1:
                return list(map(float, lines[0].split(separator)))

            for line in lines:
                matrix.append(list(map(float, line.split(separator))))

        return matrix
    except FileNotFoundError:
        print(f'Plik o nazwie {filename} nie istnieje!')

def getEigenvalues(matrix, e=10-8):
    MAX_ITERATION = 100
    A = matrix.copy()
    for i in range(MAX_ITERATION):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)

    return np.diag(A)

def maxEigenvalue(matrix, e = 10e-8):
    MAX_ITERATION = 100
    y = np.zeros_like(matrix[0])
    y[0] = 1
    
    z = np.dot(matrix, y)
    for i in range(MAX_ITERATION):
        y_new = np.divide(z, np.linalg.norm(z))
        if np.allclose(y, y_new, rtol=e):
            break
        y = y_new
        z = np.dot(matrix, y_new)
    maxEigen = np.linalg.norm(z)
    print("Max wartość własna : ", maxEigen)
    print("Odpowiadający wektor własny: ", y_new)
    
    
    

def main():
    A = matrixFromFile("A.txt")
    print("Wartosci wlasne macierzy A: ", getEigenvalues(A))

    B = matrixFromFile("B.txt")
    maxEigenvalue(B)


if __name__ == "__main__":
    main()