# To sort an array of 0,1, and 2


# Approach 1
def sortt(arr):
    L0 = []
    for i in range(len(arr)):
        if arr[i] == 0:
            L0.append(0)

    L1 = []
    for i in range(len(arr)):
        if arr[i] == 1:
            L1.append(1)

    L2 = []
    for i in range(len(arr)):
        if arr[i] == 2:
            L2.append(2)

    L = L0+L1+L2
    return L


# Approach 2 = selection sort
def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


# approach 3 = bubble sort

def bubblesort(arr):
    i = 0
    j = 0
    swapped = False
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break

    return arr

#approach = O(N) time complexity
def sorrtt(arr):
    low = 0
    mid = 0
    high = len(arr) -1
    while mid<= high:
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid +=1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1

    return arr

arr = [0,2,1,2,0]
print(sorrtt(arr))
print(bubblesort(arr))
print(selectionsort(arr))
print(sortt(arr))