#!/bin/python3


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    if (k >= 0) and (k < len(bill)):
        del bill[k]

    b_actual = int(sum(bill)/2)
    overcharge = b - b_actual

    if (overcharge > 0):
        print(overcharge)
    else:
        print('Bon Appetit')


if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
