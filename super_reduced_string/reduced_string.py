#!/bin/python3

import math
import os
import random
import re
import sys
import copy

def haha(s):
    i = 0
    while (i < len(s)-1):
        if (s[i] == s[i+1]):
            i += 2
        else:
            yield s[i]
            i += 1
    if (i<len(s)):
        yield s[len(s)-1]


# Complete the superReducedString function below.
def superReducedString(s):
    cp = copy.copy(s)
    for _ in range(len(s)//2):
        cp = list(haha(cp))

    return ''.join(cp) if (len(cp) > 0) else 'Empty String'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    # fptr.write(result + '\n')
    # fptr.close()

    print(result)
