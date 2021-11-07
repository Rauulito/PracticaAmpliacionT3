import math
import os
import random
import re
import sys
#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.

#Creameremos un metodo para ver cual es la jugada buena y asi poder ver rapidamente si el gandor es P1 o P2
def gameOfStones(n):
# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
    result = gameOfStones(n)
    fptr.write(result + '\n')
fptr.close()
