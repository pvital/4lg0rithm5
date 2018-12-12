#!/bin/python3

import re
import string
import sys

# Complete the camelcase function below.
def camelCase(s):
    words = 0
    # Check if the first letter is lowercase
    if s[0] in string.ascii_lowercase:
        words += 1
    else:
        return 0

    # Check the other words
    regex = r'[A-Z]'
    for match in re.finditer(regex, s, re.MULTILINE):
        words += 1
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(
        #    matchNum = matchNum, start = match.start(), end = match.end(),
        #    match = match.group()))
    return words

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = camelCase(s)

    #fptr.write(str(result) + '\n')
    #fptr.close()
    print(result)
