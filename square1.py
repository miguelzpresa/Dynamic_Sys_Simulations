#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

def f(x,r):
    return x + r -x**2
print("1er dyn sis \n x = a*x + b")


#initial conditions
X0 = np.arange(.1,.2,.1)
for x0 in X0:
    r = .99
    N = 20

    i = np.arange(0,N,1)
    x = x0 #variable a iterar
    X = list() #los valores generados

    for _ in i:
        X.append(x)
        x =f(x,r)
    plt.plot(X)

#plt.yscale("log")

plt.show()
 #no hemos variado la condicion inicial solo la familia de soluciones
 #graficación logartimica (no negativos ni cero)
