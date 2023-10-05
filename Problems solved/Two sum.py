# Two sum problem

def twosum(List,target):
    for i in range(len(List)):
        for j in range(i+1, len(List)):
            sum = List[i] + List[j]
            if sum == target:
                return [i,j]


L = [2,7,11,15]
target = 13
print(twosum(L,target))
L = [3,3]
target = 6
print(twosum(L,target))
