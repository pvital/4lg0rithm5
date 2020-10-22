#!/bin/python3
#
# Copyright (c) 2019 Paulo Vital
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#


def fibonacci(n: int) -> int:
    '''
    Recursive function to handle Fibonacci calculations.

    Args:
        n: int
    
    Returns:
        int
    '''
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return (fibonacci(n-2) + fibonacci(n-1))


# int main(int argc, char#*argv)
# {
#     int i, limit;
#
#     if (argc < 2) {
#         printf("Type a limit number: ");
#         scanf("%d", &limit);
#     } else {
#         limit = atoi(argv[1]);
#     }
#
#     printf("The Fibonacci sequence for %d is: ", limit);
#
#     for (i = 0; i < limit; i++)
#         printf ("%d ", fibonacci(i));
#
#     printf("\n");
#
#     return 0;
# }

if __name__ == '__main__':
    end = input('Type a limit number: ')
    sequence = []
    for i in range(int(end)+1):
        sequence.append(fibonacci(i))

    print(f'The Fibonacci sequence for {end} is: {sequence}')
        
