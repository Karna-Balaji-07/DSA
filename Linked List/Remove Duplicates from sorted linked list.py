# Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode


    def removeNode(self):
        temp= self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data ==temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head
    def printlist(self):
        temp = self.head
        L = []
        while temp is not None:
            L.append(temp.data)
            temp = temp.next
        return L

list = LinkedList()
head = None
list.push(60)
list.push(60)
list.push(60)
list.push(60)
list.push(40)
list.push(40)
list.push(30)
list.push(20)
list.push(20)
list.push(10)
list.push(10)
list.push(10)

print(list.printlist())
list.removeNode()
res = list.printlist()
print(res)
