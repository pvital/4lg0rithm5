#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    # earliers = [n for n in a if n <= 0]
    # print(earliers)
    if len([n for n in a if n <= 0]) >= k:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
