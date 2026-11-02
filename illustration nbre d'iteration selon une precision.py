# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:17:52 2026

@author: pascal
"""

import matplotlib.pyplot as plt
import numpy as np


def f1 (x: float) -> float:
    return 3*np.cos(x)-2*np.log(x+1) -1 

def ff1 (x: float) -> float:
    return -3*np.sin(x)-2/(x+1)

def f2 (x: float)-> float:
    return 9*x -3/2

def ff2 (x: float) -> float :
    return 9

def f3 (x: float) -> float:
    return (5*x -2)**3

def ff3(x: float) -> float:
    return 15*(5*x-2)**2

def f4 (x: float) -> float:
    return (2*x-1)**5
    
def ff4 (x: float) -> float:
    return 10*(2*x-1)**4

    
x = np.linspace(-0.9, 5, 1000)
y = np.linspace(-5, 5, 1000)
plt.figure()
plt.plot(x, f1(x), label = "3cos(x) - 2log(1+x) - 1")
plt.plot(y, f2(y), label = "9x - 3/2")
plt.plot(y, f3(y), label = "$(5x - 2)^3$")
plt.plot(y, f4(y), label = "$(2x - 1)^5$")
plt.title("illustration graphique des fonctions ")
plt.legend()
plt.xlim(-5,5)
plt.ylim(-8,8)
plt.grid(True)



def dichoto(f,
            a: float, 
            b: float, 
            k: int,
            nbetap = 10000)->tuple[float,int]:
    mi = (a + b)/2
    i = 0
    if a >= b:
        raise ValueError ("il faut avoir a < b")
    if f(a)*f(b) > 0:
        raise ValueError ("l'intervalle n'encadre pas une racine")
    while abs(f(mi)) >= 1/10**(k) and i < nbetap : 
        if f(mi)*f(a)<0 :
            b = mi
        else:
            a = mi
        mi = (a+b)/2
        i += 1
    if abs(f(mi)) >= 1/10**(k) :
        raise RuntimeError (" la methode n'a pas de convergence apres", nbetap, "iterations")
    return mi,i     

# print (dichoto(f1,0,1,5))

def newton (f,ff,
            a: float,
            k: int,
            nbetap = 10000) ->tuple[float,int]:
    i = 0
    while abs(f(a)) >= 1/10**(k) and i < nbetap:
        if ff(a) == 0:
            raise ZeroDivisionError("la methode de newton ne peux pas continuer" )
        x = a - f(a)/ff(a)
        a = x
        i += 1
    if abs(f(a)) >= 1/10**(k) :
        raise RuntimeError (" la methode n'a pas de convergence apres", nbetap, "iterations")
    return a, i

# print (newton(f2, ff2,0.1,5)) 

def secante (f,
             a: float,
             b: float,
             k: int,
             nbetap=10000)->tuple[float,int]: 
    i = 0
    while abs(f(b)) >= 1/10**(k) and i < nbetap:
        if (f(b)-f(a)) == 0 :
            raise ZeroDivisionError ("la méthode de la sécante ne peux pas continuer")
        x = b - f(b)*((b-a)/(f(b)-f(a)))
        a,b = b,x
        i += 1
    if abs(f(b)) >= 1/10**(k) :
        raise RuntimeError (" la methode n'a pas de convergence apres", nbetap, "iterations")
    return b, i


# print (secante(f1, 0,1,5)) 

fn = ["3cos(x) - 2log(1+x) - 1", "9x - 3/2", "$(5x - 2)^3$", "$(2x - 1)^5$"]          
funcs = [f1,f2,f3,f4]
dfuncs = [ff1,ff2,ff3,ff4]
a = 0.1
b = 1
K = np.arange(1,7)
TD = np.zeros (len(K))
TS = np.zeros (len(K))
TN = np.zeros (len(K))
for f,df,name in zip(funcs,dfuncs,fn):
    plt.figure()    
    for i in K:
        _,TD[i-1] = dichoto(f,a,b,i)
        _,TS[i-1] = secante(f,a,b,i)
        _,TN[i-1] = newton(f,df,b,i)
    print(TD,TN,TS)
    plt.plot(K,TD,".:", label = "Dichotomie")
    plt.plot(K,TS,"x:", label = "Secante")
    plt.plot(K, TN,"+:", label = "Newton")
    plt.legend()
    plt.xlabel("precision de type 10**(-k)")
    plt.ylabel("nbre d'iterations")
    plt.title("Nbre d'iterations selon la precision demandees pour la fonction {}".format(name))
    plt.grid ("True")
   