#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
def staircase(n):
    # Write your code here
    for i in range(n):
        i=i+1
        print(i*'#')
        print("\n")
#Probamos que funcione
staircase(6)

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)