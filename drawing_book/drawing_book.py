#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    book = list((i, (i+1 if i<n else 0)) for i in range(0,n+1,2))
    middle = book[int(len(book)/2)]
    flips = 0
    if (p < middle[0]):
        #print('p less than or equal to middle: %d <= %s' % (p, middle))
        for pages in book[:int(len(book)/2)]:
            if p in pages:
                return flips
            else:
                flips += 1
    else:
        #print('p greater than middle: %d > %s' % (p, middle))
        temp = book[int(len(book)/2):]
        for pages in temp[::-1]:
            if p in pages:
                return flips
            else:
                flips += 1
    return flips

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    #fptr.write(str(result) + '\n')
    #fptr.close()
    print(result)
