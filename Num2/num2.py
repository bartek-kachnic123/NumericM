from math import fabs
import numpy as np
import sys
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




def main():

    if len(sys.argv) != 4:
        print('Wrong number of args! Example: python3 num2.py A_1.txt A_2.txt B.txt')
        exit(1)

    A_1 = matrixFromFile(sys.argv[1])
    A_2 = matrixFromFile(sys.argv[2])
    B = matrixFromFile(sys.argv[3])

    bPrim = B.copy()
    bPrim[0] = bPrim[0] + 1e-5

    y_1 = np.linalg.solve(A_1, B) 
    y_2 = np.linalg.solve(A_2, B)

    y_1Prim = np.linalg.solve(A_1, bPrim)
    y_2Prim = np.linalg.solve(A_2, bPrim)
    
    print("Rozwiazanie A_1 * y1 = b  \ty1:  ", y_1)
    print("Rozwiazanie A_1 * y'1 = b' \ty'1: ", y_1Prim)
    print("Rozwiazanie A_2 * y2 = b \ty2:  ", y_2)
    print("Rozwiazanie A_2 * y'2 = b' \ty'2: ", y_2Prim)

    norm_1 = np.linalg.norm(np.subtract(y_1, y_1Prim))
    norm_2 = np.linalg.norm(np.subtract(y_2, y_2Prim))

    print("||y1-y'1|| = ", norm_1)
    print("||y2-y'2|| = ", norm_2)


  


    





if __name__ == '__main__':
    main()