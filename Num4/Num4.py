import numpy as np
import sys
import time





def backSubsitution(diagonalNum, aboveNum, resultNum, N):
   
    # Back Substition
    b = np.zeros(N)
    b[N-1] = resultNum / diagonalNum
    for i in range(N-2, -1, -1): # From N-2 to 0
        b[i] = (resultNum - ( aboveNum * b[i+1] ) ) / diagonalNum
    return b

def solve(N):
    z = backSubsitution(9, 7, 5, N)
    q = backSubsitution(9, 7, 1, N)
    b = np.zeros(N)
    sumZ = sum(z)
    sumQ = sum(q)
    for i in range(0, N): # From 0 to N-1
        
        b[i] = z[i] - (sumZ * q[i] / (1 + sumQ ))

    return b

def timeCount(N, filename="results.csv"):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("N time(N)\n")
            for n in range(1, N+1):
                start = time.perf_counter()
                solve(n)
                stop = time.perf_counter()
                
                file.write(f'{n} {stop-start}\n')
            
          
    except FileNotFoundError:
        print(f'Plik o nazwie {filename} nie istnieje!')





def main():
    N = 0
    if len(sys.argv) != 2:
        N = 50
    else: N = int(sys.argv[1]) 

    print(solve(N))
    timeCount(N)







if __name__ == "__main__":
    main()
