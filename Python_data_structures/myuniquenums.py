

def myuniquenums():
    arr=[5, 3, 3, 5,9]

    if(len(arr)==1):
        return arr[0]
    #arr = np.array(arr)
    arr.sort()
    maxidx=1
    curridx=0
    nxtidx=1
    count=0
    while (maxidx<(len(arr))):
        if(arr[curridx]==arr[nxtidx]):
            maxidx+=1
            curridx+=maxidx
            nxtidx+=curridx+1
            count=1
        else:
            count=0
            
            #return arr[curridx]

    print(arr)
    #return arr[maxidx]


print(myuniquenums())