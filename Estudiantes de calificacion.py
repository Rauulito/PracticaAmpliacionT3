#!/bin/python3
import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.# The function accepts INTEGER_ARRAY grades as parameter
#

def gradingStudents(grades):
# Write your code here
    i=0
    if(grades[i]<40):
        grades[i]
    if(grades[i]+2 % 5 == 0):
        grades[i]=grades[i]+2
    if(grades[i]+1 % 5 == 0):
            grades[i]=grades[i]+1
    else:
        grades[i]
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
