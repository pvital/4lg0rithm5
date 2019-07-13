#!/bin/python3

from myitertools import dropwhile, takewhile


def testFunction(x):
    return x < 40

if __name__ == '__main__':
    vals = [10, 20, 30, 40, 50, 40, 30]
    print(list(dropwhile(testFunction, vals)))
    print(list(takewhile(testFunction, vals)))
