#A “Palindromic Decomposition” of string S, is a decomposition of the string into substrings, 
# such that all those substrings are valid palindromes. A single character is considered a valid 
# palindrome for this problem. Print out all possible palindromic decompositions of a given string. e.g.
#  Input: abracadabra Output: a|b|r|a|c|a|d|a|b|r|a| a|b|r|a|c|ada|b|r|a| a|b|r|aca|d|a|b|r|a| 

def main():
    str='apple'

    for(int start=0, start<str.length,start++):
        String substr=str.substring(start,end)
        print(substr+ "|")

        print()


    def printSubStringSets(String str):
        List<String> resultList = new ArrayList<>();
        printSubstringSets(str, start 0 , resultList)

   
   