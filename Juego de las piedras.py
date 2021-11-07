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
def jugadaPerfecta(n):
    modulo=n%7  #Esto es asi porque lo sacamos del enunciado, esto de modulo 7 quiere decir que si tienes el numero 9 se comportara igaul que el numero 2
    piedrasExtraidas=0 #Unicamente pueden extraerse de 2,3 y 5
    if(modulo==2 or modulo==3):
        piedrasExtraidas=2
    if(modulo==4):
        piedrasExtraidas=3
    if(modulo==5 or modulo==6):
        piedrasExtraidas=5
    return piedrasExtraidas

def gameOfStones(n):
    if(jugadaPerfecta(n) != 0):
        print("P1 es el ganador")
    else:
        print("P2 es el ganador")

#Probamos que funcione
gameOfStones(9)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
    result = gameOfStones(n)
    fptr.write(result + '\n')
fptr.close()
