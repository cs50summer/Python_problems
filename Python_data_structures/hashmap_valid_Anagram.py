def hashmap_valid_anagram(s,t):
    if(len(s)!=len(t)):
        return False
    dict_s=dict()
    dict_t=dict()

    for i in s:
        if dict_s.get(i)==None:
            dict_s[i]=1
        else:
            dict_s[i]+=1
    for i in t:
        if dict_t.get(i)==None:
            dict_t[i]=1
        else:
            dict_t[i]+=1

    print(dict_s)
    print(dict_t)

    return (dict_s==dict_t)
        







print(hashmap_valid_anagram("anagram","nagaram"))