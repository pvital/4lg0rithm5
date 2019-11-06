#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    # remove the spaces of the msg
    msg = ''.join(s.split())

    # make the necessary calculations
    rows = math.floor(math.sqrt(len(msg)))
    columns = math.ceil(math.sqrt(len(msg)))

    # ensuring the area is valid
    if (rows * columns) < len(msg):
        if math.pow(rows,2) >= len(msg):
            columns = rows
        else:
            rows = columns

    # build a Genarator with the matrix of the msg
    matrix = [msg[i:(i+columns)] for i in range(0, len(msg), columns)]

    # build the return as a list. First, let's size it
    ret = []
    for _ in range(columns):
        ret.append('')

    # Now, for each part of the generator, let's pick the letters
    for txt in matrix:
        for i in range(len(txt)):
            ret[i] += txt[i]

    return ' '.join(ret)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
