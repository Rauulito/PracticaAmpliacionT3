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
    while(i<len(grades)):
        if((grades[i]+2) % 5 == 0 and grades[i]>= 40):
            grades[i]=grades[i]+2
        if((grades[i]+1) % 5 == 0 and grades[i]>=40):
            grades[i]=grades[i]+1
        i=i+1
    return grades
#Probamamos
grades= np.array([38,48,49])
print(gradingStudents(grades))
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
