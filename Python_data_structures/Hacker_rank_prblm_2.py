#!/bin/python3
# hacker_ranker_prob_time_conversion
import math
import os
import random
import re
import sys
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def timeConversion(s):
    # Write your code here
    #given input = 07:05:45PM
    if s.lower().endswith("pm"):
        hr = s.split(':')[0]
        if int(hr) < 12:
            pms_conv = int(hr) + 12   #pm sum conversion from 24 hr to military time....just need the hour
            print(pms_conv)
            new_f = s.replace(hr, str(pms_conv)).lower().replace('pm',"")
            return new_f
        elif int(hr) == 12:
            #print(s.lower().replace('pm',""))
            return s.lower().replace('pm',"")
    elif s.lower().endswith('am'):
        hr = s.split(':')[0]
        if int(hr) < 12:
            #print(s.lower().replace('am', ""))
            return s.lower().replace('am',"")
        elif int(hr)==12:
            #print(s.lower().replace(hr, '00').replace('am', ""))
            return s.lower().replace(hr, '00').replace('am', "")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()