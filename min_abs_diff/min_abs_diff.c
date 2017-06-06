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

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

#define MAX_ITEM    1000000000
#define MIN_ITEM    -1000000000

int min_abs_diff(int *array, int size)
{
    int i, j, res, min = MAX_ITEM;

    for (i = 0; i < size; i++) {
        for (j = i+1; j < size; j++) {
            res = abs(array[i] - array[j]);
            //printf("> |%d - %d| = %d\n", array[i], array[j], res);
            if (res < min)
                min = res;
        }
    }

    return min;
}

int main()
{
    int n;
    scanf("%d",&n);

    if ((n < 2) || (n > 100000)) {
        printf("ERROR: invalid parameter. The size of the series should be 2 <= n <= 10^5 \n");
        return 1;
    }

    int *a = malloc(sizeof(int) * n);
    for(int a_i = 0; a_i < n; a_i++){
        scanf("%d",&a[a_i]);
        if ((a[a_i] < MIN_ITEM) || (a[a_i] > MAX_ITEM)) {
            printf("ERROR: invalid parameter for item %d: %d. The range of elements of the series should be -10^9 <= a_i <= 10^9 \n", a_i, a[a_i]);
            return 1;
        }
    }
    printf("%d\n", min_abs_diff(a, n));
    return 0;
}
