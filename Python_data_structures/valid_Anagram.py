def valid_Anagram(s,t):
    if (len(s)!=len(t)):
        return False

    s_sort=sorted(s)
    t_sort=sorted(t)

    for i in range(len(s)):
        if s_sort[i]!=t_sort[i]:
            return False

    return True





print(valid_Anagram("anagram","nagaram"))
#assert valid_Anagram("a","agsg"), False