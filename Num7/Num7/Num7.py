import numpy as np
from matplotlib import pyplot as plt
import sys

def func(x):
    return 1 / (1 + 25 * np.power(x, 2))

def first_Func(n):
    x = np.zeros(n)
    for i in range(n): # from 0 to n - 1
        x[i] = -1 + (2 * (i / (n + 1)))
    y = np.array(list(map(func, x)))

    return x, y
        

def langrage_interpolation(x_points, y_points, x):
    n = len(x_points)
    results = y_points.copy()
    for i in range(n):
        for j in range(n):
            if (x_points[i] != x_points[j]):
                results[i] *= (x - x_points[j])
                results[i] /= (x_points[i] - x_points[j])
    return sum(results)

def calculate_points1():
    nSets = (5, 10, 25, 50)
    colors = ("red", "green", "blue", "black")
    pointsX = np.linspace(-1.0, 1.0, 256)
    pointsX = np.array(pointsX)
    pointsY = np.zeros_like(pointsX)
    pointsY2 = np.zeros_like(pointsX)
    pointsY3 = np.zeros_like(pointsX)
    pointsY4 = np.zeros_like(pointsX)

    xp, yp = first_Func(nSets[0])
    for i in range(len(pointsX)):
        pointsY[i] = langrage_interpolation(xp, yp, pointsX[i])

    xp, yp = first_Func(nSets[1])
    for i in range(len(pointsX)):
        pointsY2[i] = langrage_interpolation(xp, yp, pointsX[i])

    xp, yp = first_Func(nSets[2])
    for i in range(len(pointsX)):
        pointsY3[i] = langrage_interpolation(xp, yp, pointsX[i])
    xp, yp = first_Func(nSets[3])
    for i in range(len(pointsX)):
        pointsY4[i] = langrage_interpolation(xp, yp, pointsX[i])
    

    plt.figure(figsize=(7, 5))
        
    plt.plot(pointsX, pointsY, label=f"N={nSets[0]}", color=colors[0])
    plt.plot(pointsX, pointsY2, label=f"N={nSets[1]}", color=colors[1])
    plt.plot(pointsX, pointsY3, label=f"N={nSets[2]}", color=colors[2])
    plt.plot(pointsX, pointsY4, label=f"N={nSets[3]}", color=colors[3])
    plt.title("Interpolacja Wielomianowa Lagrange'a - Funkcja 1")
    plt.legend()

    plt.xlabel("x")
    plt.ylabel("Wn(x)")

    
    
    
    plt.yscale("log")
    plt.show()


def second_Func(n):
    x = np.zeros(n)
    pi = 3.14
    for i in range(n): # from 0 to n
        x[i] = np.cos(((2*i + 1) / (2 * (n + 1))) * pi)
    y = np.array(list(map(func, x)))

    return x, y

def calculate_points2():
    nSets = (5, 10, 25, 50)
    colors = ("red", "green", "blue", "black")
    pointsX = np.linspace(-1.0, 1.0, 256)
    pointsY = np.zeros_like(pointsX)
    pointsY2 = np.zeros_like(pointsX)
    pointsY3 = np.zeros_like(pointsX)
    pointsY4 = np.zeros_like(pointsX)

    xp, yp = second_Func(nSets[0])
    for i in range(len(pointsX)):
        pointsY[i] = langrage_interpolation(xp, yp, pointsX[i])

    xp, yp = second_Func(nSets[1])
    for i in range(len(pointsX)):
        pointsY2[i] = langrage_interpolation(xp, yp, pointsX[i])

    xp, yp = second_Func(nSets[2])
    for i in range(len(pointsX)):
        pointsY3[i] = langrage_interpolation(xp, yp, pointsX[i])

    xp, yp = second_Func(nSets[3])
    for i in range(len(pointsX)):
        pointsY4[i] = langrage_interpolation(xp, yp, pointsX[i])

    plt.figure(figsize=(7, 5))
    plt.plot(pointsX, pointsY, label=f"N={nSets[0]}", color=colors[0])
    plt.plot(pointsX, pointsY2, label=f"N={nSets[1]}", color=colors[1])
    plt.plot(pointsX, pointsY3, label=f"N={nSets[2]}", color=colors[2])
    plt.plot(pointsX, pointsY4, label=f"N={nSets[3]}", color=colors[3])


    plt.title("Interpolacja Wielomianowa Lagrange'a - Funkcja 2")
    plt.legend()

    plt.xlabel("x")
    plt.ylabel("Wn(x)")
    
    
    
    plt.yscale('log')

    
    plt.show()

def main():
    try:
        numberF = int(input("Podaj numer funkcji ( 1 lub 2) : "))
    except ValueError:
        print("ValueError")
        sys.exit(1)
        

    if numberF == 1:
        calculate_points1()
    elif numberF == 2:
        calculate_points2()
    


if __name__ == "__main__":
    main()