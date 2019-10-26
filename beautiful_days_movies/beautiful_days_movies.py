#!/bin/python3

import math
import os
import random
import re
import sys

# Returns the reverse of a given number
def reverse(n):
    rev = 0
    while (n > 0):
        reminder = n % 10
        rev = (rev * 10) + reminder
        n = n // 10
    return rev

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    total = [n for n in range(i,j+1) if (abs(n - reverse(n)) % k) == 0]
    return len(total)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(str(result))
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
