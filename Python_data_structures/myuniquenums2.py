def myuniquenums2():
    arr = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]


    if (len(arr) == 1):
        return arr[0]
    # arr = np.array(arr)
    arr.sort()
    print(arr)
    #maxidx = 2
    curridx = 0
    nxtidx = 1
    count = 0
    for i in range(len(arr)):
        if (arr[curridx] != arr[nxtidx]):
            if(curridx==0):
                return arr[curridx]
            if(nxtidx==len(arr)-1):
                return arr[nxtidx]
            if(arr[maxidx]!=arr[nxtidx]):
                print("curridx", curridx)
                print("nxtidx",nxtidx)
                return arr[nxtidx]
            #be mindful; of this change , nxtidx+1 seems bad decision
            curridx += 1
            nxtidx += 1
            maxidx = curridx + 2
        if(arr[curridx]==arr[nxtidx]):
                curridx+=1
                nxtidx+=1
                maxidx=curridx+2



    #print(arr)
    #return arr[nxtidx]


print(myuniquenums2())