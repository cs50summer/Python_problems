#Problem Statement
#Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.

def last_length(s):
    #break doen teh string at each white spce , obtain teh last string
    #len(break_s) -- length , print break_s is teh last word
    print(s)
    #global i=0
    word=[]
    break_s=s.split(" ")[-1:]
    print(len(break_s))
    print(break_s)



last_length("Hello World")




