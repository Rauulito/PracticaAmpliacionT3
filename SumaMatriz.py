import math
import os
import random
import re
import sys
import numpy as np
#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#
def simpleArraySum(ar):
# Write your code here
    sumaTotal= np.sum(ar)
    return sumaTotal

#creamos  una matriz
matriz=np.array([1,4,6],[5,9,1],[3,7,9])
print("La suma de los elementos de la matriz es:")
simpleArraySum(matriz)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
