def isValid(s):

    mystack=[]
    print(s)
    dict_brackets=dict({'(':')','[':']','{':'}'})
    pair=""
    for i in range(len(s)):
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return false
        pair=dict_brackets[s[i]]
        mystack.append(s[i])




isValid("()")