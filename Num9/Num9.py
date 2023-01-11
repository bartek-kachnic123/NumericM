import numpy as np


def F(x, n):
    return np.power(np.exp(x) - 2, n)

def bisection(n: int, a=0, b=1, epsilon=10e-10):

    if F(a,n) * F(b,n) > 0:
        print("f(a) and f(b) must have values of diffrent sign")
        return

    x_steps = []
    xi = a
    while np.abs(b - a) > epsilon:
        xi = (a + b) / 2
        x_steps.append(xi)

        if np.abs(F(xi, n)) <= epsilon:
            break

        if F(a, n) * F(xi, n) < 0:
            b = xi
        else:
            a = xi
    numSteps = len(x_steps)
    print(f"Ilość kroków bisekcji: {numSteps}\t x* = {x_steps[-1]}")

    writeToFile(f'{bisection.__name__}{n}.csv', x_steps, numSteps)
    
   

def falsi(n: int, a=0, b=1, epsilon=10e-10):

    if F(a,n) * F(b,n) > 0:
        print("f(a) and f(b) must have values of diffrent sign")
        return

    x_steps = []
    xi = (a*F(b, n) - b*F(a, n)) / (F(b, n) - F(a, n)) # x1
    while np.abs(F(xi, n)) > epsilon:

        x_steps.append(xi)

        if F(a, n) * F(xi, n) >= 0:
            xi = (xi*F(a, n) - a*F(xi, n)) / (F(a,n) - F(xi,n))
        else:
            xi = (xi*F(b, n) - b*F(xi, n)) / (F(b,n) - F(xi,n))

    numSteps = len(x_steps)
    print(f"Ilość kroków falsi: {numSteps}\t x* = {x_steps[-1]}")

    writeToFile(f'{falsi.__name__}{n}.csv', x_steps, numSteps)

def writeToFile(filename: str, x_steps: list[float], numSteps: int):
     with open(filename, mode='w', encoding='utf-8') as file:
        
        for i in range(numSteps):
            file.write(f'{i+1};{np.abs(x_steps[i] - x_steps[-1])}\n')

def main():
    
    bisection(1)
    #bisection(2)
    bisection(3)

    falsi(1)
    #falsi(2)
    #falsi(3) too long to find
    

if __name__ == "__main__":
    main()