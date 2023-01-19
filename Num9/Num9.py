import numpy as np


def F(x, n):
    return np.power(np.exp(x) - 2, n)

def bisection(n: int, F, a=0, b=1, epsilon=10e-10):

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
    print(f"Ilość kroków {bisection.__name__} n={n}: {numSteps}\t x* = {x_steps[-1]}")

    writeToFile(f'{bisection.__name__}{n}.csv', x_steps, numSteps)
    
def falsi(n: int, F, a=0, b=1, epsilon=10e-10):

    if F(a,n) * F(b,n) > 0:
        print("f(a) and f(b) must have values of diffrent sign")
        return

   
    if (n==3):
        def F_derivate(x, *args):
            return (np.exp(x) - 2) * (np.exp(x) / n)
        F = F_derivate # change function to derivate

    x_steps = []
    xi = (a*F(b, n) - b*F(a, n)) / (F(b, n) - F(a, n)) # x1
    while np.abs(F(xi, n)) > epsilon:

        x_steps.append(xi)

        if F(a, n) * F(xi, n) >= 0:
            xi = (xi*F(a, n) - a*F(xi, n)) / (F(a,n) - F(xi,n))
        else:
            xi = (xi*F(b, n) - b*F(xi, n)) / (F(b,n) - F(xi,n))

    numSteps = len(x_steps)
    print(f"Ilość kroków {falsi.__name__} n={n}: {numSteps}\t x* = {x_steps[-1]}")

    writeToFile(f'{falsi.__name__}{n}.csv', x_steps, numSteps)

def secant(n: int, F, a=0, b=1, epsilon=10e-10):

    if F(a,n) * F(b,n) > 0:
        print("f(a) and f(b) must have values of diffrent sign")
        return
    xi = b
    x_steps = []
    while np.abs(F(xi, n)) > epsilon:
        xi = (a*F(b, n) - b*F(a, n)) / (F(b,n) - F(a,n))
        x_steps.append(xi)
        b, a= xi, b # swap

    numSteps = len(x_steps)
    print(f"Ilość kroków {secant.__name__} n={n}: {numSteps}\t x* = {x_steps[-1]}")

    writeToFile(f'{secant.__name__}{n}.csv', x_steps, numSteps)

def newton(n: int, F, x0=1, epsilon=10e-10):
    def G(x):
        return (np.exp(x) - 2) / (np.exp(x) * n)
    x_steps = []

    while np.abs(F(x0, n)) > epsilon:
        x0 = x0 - G(x0)
        x_steps.append(x0)
    
    numSteps = len(x_steps)
    print(f"Ilość kroków {newton.__name__} n={n}: {numSteps}\t x* = {x_steps[-1]}")

    writeToFile(f'{newton.__name__}{n}.csv', x_steps, numSteps)

def writeToFile(filename: str, x_steps: list[float], numSteps: int):
     with open(filename, mode='w', encoding='utf-8') as file:
        file.write("n;|x-x*|\n")
        for i in range(numSteps):
            file.write(f'{i+1};{np.abs(x_steps[i] - x_steps[-1])}\n')

def main():
    
    bisection(1, F)
    #bisection(2) F(x) >= 0 always
    bisection(3, F)

    falsi(1, F)
    #falsi(2) F(x) >= 0 always
    falsi(3, F) # upgraded from  around 300k to 10 iterations

    secant(1, F)
    #secant(2, F) F(x) >= 0 always
    secant(3, F)
    
    newton(1, F)
    newton(2, F)
    newton(3, F)

if __name__ == "__main__":
    main()