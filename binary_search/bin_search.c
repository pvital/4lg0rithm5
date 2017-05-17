/*
 * Copyright (c) 2017 Paulo Vital
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE  10

int bin_search(int *array, int target)
{
    int begin, end, middle;

    begin = 0;
    end = ARRAY_SIZE - 1;

    while (begin <= end) {
        middle = (begin + end) / 2;
        printf("begin: %d, middle: %d, end: %d\n", begin, middle, end);

        if (array[middle] == target)
            return middle;

        if (array[middle] < target) {
            begin = middle + 1;
            continue;
        }

        if (array[middle] > target) {
            end = middle - 1;
            continue;
        }
    }

    return -1;
}

int main(void)
{
    int *array;
    int i, target, index;

    array = (int *) malloc(sizeof(int) * ARRAY_SIZE);
    for (i = 0; i < ARRAY_SIZE; i++) {
        array[i] = i+1;
    }
    target = 7;
    index = -1;

    index = bin_search(array, target);

    if (index < 0) {
        printf("ERROR - negative index: %d\n", index);
        free(array);
        return 0;
    }
    printf("The target %d found at index %d.\n", target, index);

    free(array);
    return 0;
}
