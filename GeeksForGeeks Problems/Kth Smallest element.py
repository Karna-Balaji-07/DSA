# Kth smallest element

# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.


def smallest1(arr,n,k):
    L = arr
    L.sort()
    return L[k-1]

def smallest2(arr,starting_index,ending_index,n):
    L = arr
    L.sort()
    l = L[starting_index:ending_index]
    return l[0]

arr = [7,10,4,3,20,15]
n = len(arr)
k = 3
starting_index = 4
ending_index = len(arr)
print(smallest2(arr,starting_index-1,ending_index,n))
print(smallest1(arr,n,k))