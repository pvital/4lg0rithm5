#!/bin/python3

def countingValleys(n, s):
    level = 0
    valleys_walked = 0
    for step in s:
        prev_level = level
        level += 1 if step == 'U' else -1
        # a valley is walked ONLY when level == -1 (1 step below sea level)
        # and coming from sea level (level 0)
        valleys_walked += 1 if ((level == -1) and (prev_level == 0)) else 0
        # print(prev_level, step, level, valleys_walked)

    return valleys_walked

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result))

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
