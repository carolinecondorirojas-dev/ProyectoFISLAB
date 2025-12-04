import math

def errorX(xexp, t, A, w, B):
    errores = [0] * len(xexp)

    for i in range(len(xexp)):
        xmod = A * math.cos(w * t[i] + B)
        errores[i] = abs(xexp[i] - xmod)

    return errores


def errorV(vexp, t, A, w, B):
    errores = [0] * len(vexp)

    for i in range(len(vexp)):
        vmod = -w * A * math.sin(w * t[i] + B)
        errores[i] = abs(vexp[i] - vmod)

    return errores


# MAIN para pruebas rápidas
if __name__ == "_main_":
    x = [1, 0.8, 0.3]
    v = [0, -2, -3]
    t = [0, 0.1, 0.2]

    A = 1
    w = 5
    B = 0.2

    ex = errorX(x, t, A, w, B)
    ev = errorV(v, t, A, w, B)

    for e in ex:
        print("Error X =", e)
    for e in ev:
        print("Error V =", e)