from math import exp

def zeroum(n=0):
    if n > 0:
        return 1
    else:
        return 0

def s(n=0):
    if n < -1:
        return -1
    elif n > 1:
        return 1
    else:
        return n

def soma(n):
    s = 0
    for i in n:
        s += i
    return s

def sigmoid(x):
    return 1/(1+exp(-x))

def reta(x):
    return x