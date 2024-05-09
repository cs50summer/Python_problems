import math
import os
import random
import re
import sys


#
#next hackerrank problem from day 2 : absolute difference of diagonals within a square matrix:
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

def diagonalDifference(arr):
    # Write your code here
    print(arr)
    lds = []
    rds = []
    for i in range(len(arr)):
        for j in range(len(arr)):

            #need to compute sum of left diagonal:
            if i == j:
                lds.append(arr[i][j])
            #print(sum(lds))

            #now calculating sum of right diagonal:
            if i + j == len(arr)-1:
                rds.append(arr[i][j])
            #print(sum(rds))
    return (abs(sum(lds) - sum(rds)))




result = diagonalDifference(arr)
print(result)














