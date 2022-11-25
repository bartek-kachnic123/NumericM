import numpy as np
import sys
MAX_ITERATION = 100

def solveJacobi(N, start_number ,diagonalNum=3, firstAboveNUM=1, secondAboveNUM=0.2, result = None):
    x = np.arange(1, N+1)
    b = start_number

    
    for k in range(0, MAX_ITERATION):
        b_new = np.zeros(N)
        # current solution 
        if result is None:
            pass
        else:
            error = np.fabs(np.linalg.norm(result)-np.linalg.norm(b))
            
            #print(f"Error iteration nr {k} = {error}")
            print(f"{k} {error}")

        # sum2
        sum2 = 0
        # sum1
        sum1 = 0
        # srodek
        for i in range(0, N):

            # Calc sum1
            if i == 0: 
                pass # sum1 = 0
            elif i == 1:
                sum1 = firstAboveNUM*b[i-1]
            else:
                sum1 = secondAboveNUM * b[i-2] + firstAboveNUM * b[i-1]

            # Calc sum2
            if i == N-1:
                sum2 = 0
            elif i == N-2:
                sum2 = firstAboveNUM * b[i+1]
            else:
                sum2 = firstAboveNUM*b[i+1]+secondAboveNUM*b[i+2]
            
            # Results
            b_new[i] = (x[i] - sum1 - sum2) / diagonalNum
            
        # jesli blad przyblizenia jest < 1e-8
        if np.allclose(b, b_new, rtol=1e-8):
            return b
        b = b_new

count = 1

def solveGauss_Seidla(N, start_number ,diagonalNum=3, firstAboveNUM=1, secondAboveNUM=0.2, result = None):

    x = np.arange(1, N+1)
    b = start_number

    
    for k in range(0, MAX_ITERATION):
        b_new = np.zeros(N)
        # current solution 
        if result is None:
            pass
        else:
            error = np.fabs(np.linalg.norm(result)-np.linalg.norm(b))
            #print(f"Error iteration nr {k} = {error}")
            print(f"{k} {error}")

        # sum2
        sum2 = 0
        # sum1
        sum1 = 0
        # srodek
        for i in range(0, N):

            # Calc sum1
            if i == 0: 
                pass # sum1 = 0
            elif i == 1:
                sum1 = firstAboveNUM*b_new[i-1]
            else:
                sum1 = secondAboveNUM * b_new[i-2] + firstAboveNUM * b_new[i-1]

            # Calc sum2
            if i == N-1:
                sum2 = 0
            elif i == N-2:
                sum2 = firstAboveNUM * b[i+1]
            else:
                sum2 = firstAboveNUM*b[i+1]+secondAboveNUM*b[i+2]
            
            # Results
            b_new[i] = (x[i] - sum1 - sum2) / diagonalNum
            
        # jesli blad przyblizenia jest < 1e-8
        if np.allclose(b, b_new, rtol=1e-8):
            return b
        b = b_new
        
        





def main():
    N = 0 # length of array
    if len(sys.argv) != 2:
        N = 100
    else:
        N = int(sys.argv[1])
    # START POINT [0, 0,....0]
    print("Gauss-Seidla method: ")
    result = solveGauss_Seidla(N, np.zeros(N))
    print(result)
    solveGauss_Seidla(N, np.zeros(N), result=result)
  
    print("Jacobi method: ")
    result = solveJacobi(N, np.zeros(N))
    print(result)
    solveJacobi(N, np.zeros(N), result=result)
    print()
    print("Random version")
    random_arr = np.random.rand(N)*10
    random_arr2 = random_arr.copy()
    print("Gauss-Seidla method: ")
    result = solveGauss_Seidla(N, random_arr)
    print(result)
    solveGauss_Seidla(N, random_arr, result=result)

    print("Jacobi method: ")
    result = solveJacobi(N, random_arr2)
    print(result)
    solveJacobi(N, random_arr2, result=result)


if __name__ == '__main__':
    main()