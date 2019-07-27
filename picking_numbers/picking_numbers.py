#!/bin/python3

import math
import os
import random
import re
import sys

#
# Generator method to buld a list containing only the elements with diff <= 1
#
def genSucessors(pivot, array):
    for i in array:
        if (abs(pivot - i) <= 1):
            yield i

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
    a.sort()
    max = 2
    for i in range(0,len(a)):
        size = len(list(genSucessors(a[i], a[i:])))
        if (size > max):
            max = size

    return max


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    #fptr.write(str(result) + '\n')
    #fptr.close()
    print(result)
