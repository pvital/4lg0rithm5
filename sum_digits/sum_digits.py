def split(n):
    '''
    Split a positive number (n) into all but its last digit and its last digit.
    '''
    return n // 10, n % 10


def sum_digits(n):
    '''
    Return the sum of the digits of a positive integer n.
    '''
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
