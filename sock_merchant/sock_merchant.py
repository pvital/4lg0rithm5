#!/bin/python3

import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result = 0
    for xi in range(n):
        x = ar[xi]
        for yi in range(xi+1, len(ar)):
            y = ar[yi]
            if x == y:
                del ar[xi]
                del ar[yi-1]
                return sockMerchant(len(ar), ar) + 1
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    #fptr.write(str(result) + '\n')
    #fptr.close()
    print(result)
