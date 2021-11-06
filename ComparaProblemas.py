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
    i=0
    while(i<len(a)):
        if a[i]<b[i]:
            PuntuacionCarlos= PuntuacionCarlos + 1
        if a[i]>b[i]:
            PuntuacionLucia= PutuacionLucia + 1
        else:
            print("Ls puntuaciones no varian en esta comparacion porque tienen los mismos puntos")
        i=i+1
        return MatrizResultado
#Probamos que funcione
a=np.array([3,8,6])
b=np.array([5,7,6])
print("La matriz de retorno de la puntuación de Lucia y de Carlos es:")
print(compareTriplets(a,b))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
