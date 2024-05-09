#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

def isPalindrome(x):
    # reverse x and store it in a variable
    tmp=x
    if(x==0):
        return True

    y=0
    while x>0:
        y=(y*10)+(x%10)
        x=(x//10)

    if tmp-y==0:
        return True
    else:
        return False


print(isPalindrome(22))


