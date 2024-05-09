#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Sorting teh two string to arrange it in alphabetical order
    a_std=sorted(a)
    b_std=sorted(b)
    #print the sorted arrays
    print(a_std)
    print(b_std)
    #Initialize the dictionaries for two arrays
    ad=dict()
    bd=dict()
    output=0

    #Add key as character and value as number of occurences in the array
    for i in a_std: #"abcd
        if ad.get(i)==None:
            ad[i]=1
        else:
            ad[i]+=1
    for i in b_std:#abcde
        if bd.get(i) == None:#abcde
            bd[i] = 1
        else:
            bd[i] += 1

    #print the two dictionaries
    print(ad)
    print(bd)


    #how do you compare key values of each dict to another
    for i in ad: #{'a': 1, 'b': 1, 'c': 1, 'd': 1}
        if (bd.get(i)== None): #'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
            output+=ad.get(i)

        else:
            output+=abs(bd.get(i)-ad.get(i))

    for i in bd:
        if (ad.get(i)== None):
            output+=bd.get(i)

        else:
            output+=abs(bd.get(i)-ad.get(i))

    print("output:" ,output)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = input()

    #b = input()

    a="fcrxzwscanmligyxyvym"
    b="jxwtrhvujlmrpdoqbisbwhmgpmeoke"

    res = makeAnagram(a, b)

    #fptr.write(str(res) + '\n')

    #fptr.close()
