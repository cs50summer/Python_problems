# Given a Roman numeral , convert it into integer

# Store Roman numeral to Integer into a dictionary 
# Iterate through all roman numerals in a loop 
# Introduce proper operations to evaluate place value once roman to integer conversion is done 
# Add all values iteratively into a sum . The final value is a Integer .
def romanToInt(s):
    Int_value1=0
    prev_value=0
    sum=0
    roman_to_int = dict({'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})
    print(roman_to_int)

    for i in range(len(s)):
        if s[i] in roman_to_int.keys():
            Int_value1 = roman_to_int[s[i]]
            if(prev_value!=0 and prev_value<Int_value1):
                Int_value1=Int_value1-prev_value-prev_value

            sum=sum+Int_value1
            prev_value=Int_value1
            print("i", i)
            print(Int_value1)
            print("Sum",sum)
    return sum


print(romanToInt("IVIX"))