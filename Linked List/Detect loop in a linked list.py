# Detect loop in a linked list

# Detect loop in a linked list by modification in Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectloop(temp):
    while temp is not None:
        if temp.flag == 1:
            return True

        temp.flag = 1
        temp = temp.next
    return False


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        newNode.flag = 0
        self.head = newNode

    def printlist(self):
        temp = self.head
        L = []
        while temp:
            L.append(temp.data)
            temp = temp.next
        return L


list = LinkedList()
head = None
list.push(10)
list.push(20)
list.push(30)
list.push(40)
list.push(50)
list.push(60)
res = list.printlist()
print(res)
print()

list.head.next.next.next.next = list.head.next
if detectloop(list.head):
    print(1)
else:
    print(0)


