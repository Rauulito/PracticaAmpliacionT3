#!/bin/python3
import math
import os
import random
import re
import sys
import numpy as np
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
# Write your code here
#Creamos variables para guardar las puntuaciones de Carlos y Lucia
    PuntuacionCarlos=0
    PutuacionLucia=0
#Creamos matriz donde resolveremos el resultado
    MatrizResultado= np.array([PuntuacionCarlos,PutuacionLucia])
    if a[0]<b[0]:
        PuntuacionCarlos= PuntuacionCarlos + 1
    if a[0]>b[0]:
        PuntuacionLucia= PuntuacionLucia + 1
    else:
        print("Ls puntuaciones no varian en esta comparacion porque tienen los mismos puntos")

    if a[1]<b[1]:
            PuntuacionCarlos= PuntuacionCarlos + 1
    if a[1]>b[1]:
        PuntuacionLucia= PuntuacionLucia + 1
    else:
        print("Ls puntuaciones no varian en esta comparacion porque tienen los mismos puntos")

    if a[2]<b[2]:
            PuntuacionCarlos= PuntuacionCarlos + 1
    if a[2]>b[2]:
        PuntuacionLucia= PuntuacionLucia + 1
    else:
        print("Ls puntuaciones no varian en esta comparacion porque tienen los mismos puntos")

    return MatrizResultado

if __name__ == '__main__':
fptr = open(os.environ['OUTPUT_PATH'], 'w')
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
fptr.write(' '.join(map(str, result)))
fptr.write('\n')
fptr.close()