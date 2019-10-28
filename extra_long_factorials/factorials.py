#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    for i in reversed(range(1,n)):
        n *= i
    return n

if __name__ == '__main__':
    n = int(input())
    result = extraLongFactorials(n)
    print(result)
