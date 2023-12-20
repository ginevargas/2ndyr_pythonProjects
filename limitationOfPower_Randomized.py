# Learning Task (Limitation of Power)
# Group7_Vargas_DimanarigArjunRashid
# Proposed solution for Randomized Algorithm Problem

import random

def getRandom(x,y):
    tmp=(x + random.randint(0,100000) % (y-x+1))
    return tmp
# randomized binary search function
def randomizedBinarySearch(arr,l,r,x) :
    if r>=l:

        # Here we have defined middle as
        # random index between l and r ie.. [l, r]
        mid=getRandom(l,r)

        # If the element is present at the
        # middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then
        # it is present in left subarray
        if arr[mid]>x:
            return randomizedBinarySearch(arr, l, mid-1, x)

        # Else the element is present in right subarray
        return randomizedBinarySearch(arr, mid+1,r, x)

    # when element is not present
    return -1

# Driver code
if __name__=='__main__':
    arr = [2, 3, 4, 10, 40, 21, 20, 78, 69, 99]
    n=len(arr)

    #ask for an element of an array to be search
    x=int(input("Enter the element of an array: "))

    #display the results
    result = randomizedBinarySearch(arr, 0, n - 1, x)
    if result == -1:
        print('Element is not found')
    else:
        print('Element is found at index ', result)

