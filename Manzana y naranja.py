#!/bin/python3
import math
import os
import random
import re
import sys
import numpy as np
#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
# 1. INTEGER s
# 2. INTEGER t
# 3. INTEGER a
# 4. INTEGER b
# 5. INTEGER_ARRAY apples
# 6. INTEGER_ARRAY oranges
#

# Write your code here
def countApplesAndOranges(s, t, a, b, manzanas, naranjas):
    # Write your code here
    manzanasDentro=0
    naranjasDentro=0

    i=0
    while(i<len(manzanas)):
        if((a+manzanas[i])>=s and (a+manzanas[i])<=t):
            manzanasDentro = manzanasDentro+1
        i=i+1

    i=0
    while(i<len(naranjas)):
        if((b+naranjas[i])>=s and (b+naranjas[i])<=t):
            naranjasDentro = naranjasDentro+1
        i=i+1

    print("El número de manzanas que caen en la casa de Sam: ")
    print(manzanasDentro)
    print("El número de naranjas que caen en la casa de Sam: ")
    print(naranjasDentro)

#Probamos
s=7
t=11
a=5
b=15
manzanas=np.array([-2,2,1,3])
naranjas=np.array([5,-6,1,-7])
countApplesAndOranges(s, t, a, b, manzanas, naranjas)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges