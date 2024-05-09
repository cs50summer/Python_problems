def searchInsert(nums, target):
    for i in range(len(nums)-1):
	        if (nums[i] >= target):
                   return (i)
    i=i+2
    return(i)


print(searchInsert([1,3,5,8,9,10],11))

"""
sorted
array - - no
repetitive

ex: [1, 3, 5, 6] - tar = 4 - - normal
within
the
for loop, the solution can be obtained
ex: tar = 0
ex: tar = 7

1.
iterate
through
the
loop
2.
compare
each
array
value
to
the
target
value
a. if arr[i] < tar, proceed
through
the
loop - -
b. if arr[i] > tar, note
down
the
index
of
that
array
value
return i: because
there
are
distinct
integers and also
find
i
3. if target == arr[i],
return i
4.
the
end
of
loop

return (i + 1)


def sip(arr, tar):
    for i in range len(arr)-1:
        if (arr[i] >= tar):
            # that means the target should be just before this integer , in other words , this position , if replaced in a sorted array 
            return i
    # if the target if greater than the last element , and the looping ends , then return the index value after the looping 
    return (i + 1)


"""