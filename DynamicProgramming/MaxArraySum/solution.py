#!/bin/python3

import math
import os
import random
import re
import sys
import time

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    arr[2] = max(arr[2], arr[0], arr[0] + arr[2])
    max_sum = max(arr[0], arr[1], arr[2])
    for i in range(3, len(arr)):
        arr[i] = max(
            arr[i], arr[i - 2], arr[i - 3],
            arr[i - 2] + arr[i], arr[i - 3] + arr[i]
        )
        max_sum = max(max_sum, arr[i])

    return max_sum

if __name__ == '__main__':
    input_file = input('Enter the input file: ')
    fptr = open(input_file, 'r')
    n = int(fptr.readline())
    arr_str = fptr.readline()
    fptr.close()

    arr = list(map(int, arr_str.rstrip().split()))

    res = maxSubsetSum(arr)

    print(str(res) + '\n')
