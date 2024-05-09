import statistics
#import numpy as np

def findMedian(arr):
    # Write your code here
    #print(sorted(arr))
    s_arr = sorted(arr)
    for i in range(len(s_arr)):
        return statistics.median(s_arr)

print(findMedian([1,2,3,8,9,7]))