# merge sort
def merge(arr,low,mid,high):
    n1 = mid-low+1
    n2 = high-mid

    left = [0] * n1
    right = [0] * n2

    for i in range(0,n1):
        left[i] = arr[low+i]

    for i in range(0,n2):
        right[i] = arr[mid+1+i]

    i = 0 # index of first array
    j = 0 # index of second array
    k = low #index of merged array

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1



def mergesort(arr,left,right):
    if left< right:
        mid = left + (right-left)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left,mid,right)


arr = [12,11,13,5,6,7]
n = len(arr)
mergesort(arr,0,n-1)
for i in range(n):
    print(arr[i],end=" ")
