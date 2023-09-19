# Find duplicates in an array

# Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1].

def duplicates(arr,n):
    duplicate = []
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                dup = arr[i]
                if dup not in duplicate:
                    duplicate.append(dup)
                    duplicate.sort()
    if len(duplicate) == 0:
        return -1
    else:
        return duplicate

def Duplicate(arr,n):
    dup = arr
    dup.sort()
    L = []
    i = 0
    while i < (n-1):
        if arr[i] == arr[i+1]:
            dupli = arr[i]
            if dupli not in L:
                L.append(arr[i])

        i+=1

    if len(L) == 0:
        return [-1]
    else:
        return L


def duplicates1(arr,n):
    for i in range(0, n):
        index = arr[i] % n
        arr[index] += n

        # Now check which value
        # exists more
        # than once by dividing
        # with the size
        # of array
    flag = False
    res = []
    for i in range(0, n):
        if (arr[i] // n) > 1:
            res.append(i)
            flag = True

    if flag == False:
        res.append(-1)
    return res

    # for i in range(0,n):
    #     index = arr[i] % n
    #     arr[index] += n
    #
    # flag = False
    # duplicatel = []
    # for i in range(0,n):
    #     if(arr[i]//n) > 1:
    #         duplicatel.append(i)
    #         flag = True
    #
    # if flag == False:
    #     duplicatel.append(-1)
    #
    # return duplicatel



arr = [2,3,1,2,3,0]
arr = [0,4,1,2]
n = len(arr)
print(duplicates1(arr,n))
print(Duplicate(arr,n))
print(duplicates(arr,n))