#!/bin/python3

import math
import os
import random
import re
import sys

def isScoreInTheBoard(score, board):
    '''
    Function to check if there is a given score in the (dictionary) board,
    returning the rank of the board if existent, otherwise, return 0
    '''
    for k,v in board.items():
        if score in v:
            return k
    return 0

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    res = []
    leaderboard = {}

    for alice_score in alice:
        # Append the new score to the scores board and sort it.
        scores.append(alice_score)
        scores.sort(reverse=True)

        # Get the position of the new score
        last = i = 0
        for item in scores[:scores.index(alice_score)]:
            if (item != last):
                i += 1
                last = item
        res.append(i+1)

        # Clean the scores board
        scores.remove(alice_score)

    return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
    print('\n'.join(map(str, result)))
