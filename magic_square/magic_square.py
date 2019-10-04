#!/bin/python3

import math
import os
import random
import re
import sys

def genColumns(matrix, i):
    for line in matrix:
        yield line[i]


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    sum_columns = []
    sum_lines=[]
    for i in range(3):
        sum_lines.append(sum(s[i]))
        sum_columns.append(sum(list(genColumns(s,i))))
    print(sum_lines)
    print(sum_columns)

    sum_diff = 0
    for line in s:
        sum_diff += abs(15 - sum(line))
    return sum_diff

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    # fptr.write(str(result) + '\n')
    # fptr.close()

    print(result)
