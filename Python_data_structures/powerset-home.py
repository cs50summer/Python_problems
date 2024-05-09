def powerset(ary,i,result,j):
    if(i==3):
        print("{")
        for index in range (j):
            print(result[j])
            if((index+1)!=j):
                print(",")
        print("}")
        return


    result[j]=ary[i]
    powerset(ary,i+1,result,j+1)

    powerset(ary,i+1,result,j)
    return


#def main():
    #ary=[1,2,3]
powerset(ary[1,2,3],0,result,0)
