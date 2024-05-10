#Given a roman numeral, convert it to an integer.

# Pseudocode :
# A dictionary stores key value pair for each roman symbol to integer value 
# Initialize the 3 digits where a roman number is stored after getting evaluated 
# For every digit look uo the corresponding integer value and store it in the variable 
# If roman numeral contains length more than 1 store it in correspoding place value integer 
# add all place values to find teh sum and hence teh integer valu of the corresponding roman number 
# final sum holds teh integer value 


def romanToInt(s):
    Int_value1=0
    Int_value2=0
    Int_value=0
    sum=0

    roman_to_int = dict({'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})
    print(roman_to_int)
    for i in range(len(s)):
        if s[i] == "I":
            Int_value = 1
            # print(Int_value)
        if s[i] == "V":
            Int_value = 5
        if s[i] == "X":
            Int_value = 10
        if s[i] == "L":
            Int_value = 50
        if s[i] == "C":
            Int_value = 100
        if s[i] == "D":
            Int_value = 500
        if s[i] == "M":
            Int_value = 1000
        if len(s)==0:
            sum=sum+Int_value
            return sum
        elif len(s)>1:
            if s[i] in roman_to_int.keys():
                Int_value1=roman_to_int[s[i]]
                print("i",i)
                print(Int_value1)
            if s[i+1] in roman_to_int.keys():
                Int_value2=roman_to_int[s[i+1]]
                print(Int_value2)
            if(Int_value2>Int_value1):
                sum=sum+Int_value2-Int_value1
            if(Int_value2<=Int_value1):
                sum=sum+Int_value1+Int_value2
        if((i+1)>=len(s)):
            break

    return sum


romanToInt("II")