#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'balancedOrNot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY expressions
#  2. INTEGER_ARRAY maxReplacements
#

def balancedOrNot(expressions, maxReplacements):
    # Write your code here
    ret = []
    #print(expressions, maxReplacements)
    for i in range(len(expressions)):
        expr = expressions[i]
        maxReplacement = maxReplacements[i]
        replacementMade = 0
        newExpr = []

        print(expr, maxReplacement)
        # j = 0
        # while (j < len(expr)):
        #     if (j == (len(expr)-1)):
        #         print('entrou aki 1')
        #         replacementMade += 1
        #         break
        #     else:
        #         if ((expr[j] == '<') and (expr[j+1] == '>')):
        #             print(expr[j], expr[j+1], j, replacementMade)
        #             j += 2
        #         elif (expr[j] == '>'):
        #             print(expr[j], j, replacementMade)
        #             j += 1
        #             replacementMade += 1
        #         else:
        #             print(expr[j], j, replacementMade)
        #             j += 1

        # for item in expr:
        #     if (item == '<'):
        #         newExpr.append('<')
        #     else:
        #         if newExpr:
        #             newExpr.pop()
        #         else:
        #             replacementMade += 1
        #
        for i in range(len(expr)):
            if (expr[i] == '>'):
                if not (expr[i-1] == '<'):
                    replacementMade += 1
        print(replacementMade)
        ret.append(1 if (replacementMade == maxReplacement) else 0)

    return ret

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    expressions_count = int(input().strip())

    expressions = []

    for _ in range(expressions_count):
        expressions_item = input()
        expressions.append(expressions_item)

    maxReplacements_count = int(input().strip())

    maxReplacements = []

    for _ in range(maxReplacements_count):
        maxReplacements_item = int(input().strip())
        maxReplacements.append(maxReplacements_item)

    result = balancedOrNot(expressions, maxReplacements)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

    print('\n'.join(map(str, result)))
