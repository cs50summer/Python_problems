#!/bin/python3
# hacker_ranker_prob_time_conversion
# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
#timeConversion has the following parameter(s):
#string s: a time in  hour format
#Returns string: the time in  hour format
#Input Format
#A single string  that represents a time in -hour clock format (i.e.:  or ).

#Solution 
# Spilt the string input and store only the hour number inside the 'hr' variable
# If hour is less than 12  lets say 8 and ends with pm ie. night time , tehn add 12 to make it 20 and store it as 20.00 stripping off am or pm 
# if hour is 12 then strip off only pm or am 
# If hour is am then stip off only am 

import math
import os
import random
import re
import sys

def timeConversion(s):
    
    if s.lower().endswith("pm"):
        hr = s.split(':')[0]
        if int(hr) < 12:
            pms_conv = int(hr) + 12   #pm sum conversion from 24 hr to military time....just need the hour
            print(pms_conv)
            new_f = s.replace(hr, str(pms_conv)).lower().replace('pm',"")
            return new_f
        elif int(hr) == 12:
            return s.lower().replace('pm',"")
    elif s.lower().endswith('am'):
        hr = s.split(':')[0]
        if int(hr) < 12:
            return s.lower().replace('am',"")
        elif int(hr)==12:
           return s.lower().replace(hr, '00').replace('am', "")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()