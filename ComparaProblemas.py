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
    puntuacionCarlos=0
    putuacionLucia=0

    i=0
    while(i<len(a)):
        if a[i]<b[i]:
            puntuacionCarlos= puntuacionCarlos + 1
        if a[i]>b[i]:
            puntuacionLucia= putuacionLucia + 1
        i=i+1

    print(puntuacionCarlos)
    print(puntuacionLucia)
    matrizResultante= np.array([puntuacionLucia,puntuacionCarlos])
    return matrizResultante

#Probamos que funcione
a=np.array([3,8,6])
b=np.array([2,4,5])
print(len(a))
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
