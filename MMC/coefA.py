def calcularA(x):
    xmax = 0
    for xi in x:
        if abs(xi) > xmax:
            xmax = abs(xi)
    return xmax


if __name__ == "__main__":
    x = [1.2, -1.5, 1.4, -1.52]
    A = calcularA(x)
    print("Coeficiente A =", A)