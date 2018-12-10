#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def getMinUniqueSum(arr):
    ret = 0
    tmp = arr.copy()
    used = []
    for x in tmp:
        if (arr.count(x) > 1) and (x not in used):
            print('entrou aqui 1 com %d' % x)
            ret += x+1
            used.append(x)
            print(ret)
        else:
            print('entrou aqui 2 com %d' % x)
            ret += x
            print(ret)
    return ret

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #n = int(input())
    arr = [10, 1, 5, 2, 2]
    result = getMinUniqueSum(arr)
    #fptr.write(str(result) + '\n')
    #fptr.close()
    print(result)
