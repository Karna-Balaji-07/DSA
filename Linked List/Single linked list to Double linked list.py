# Convert single linked list to double linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printsinglelinkedlist(self):
        temp = self.head
        L = []
        while temp:
            L.append(temp.data)
            temp = temp.next
        return L

    def circularlinkedlist(self):
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = self.head
                break
            temp = temp.next
        return True

    def printcircularlinkedlist(self):
        temp =  self.head
        K = []
        original_head = self.head
        while temp:
            K.append(temp.data)
            temp = temp.next
            if temp == original_head:
                break
        return K

llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)

print(llist.printsinglelinkedlist())
# llist.circularlinkedlist()
# print(llist.printcircularlinkedlist())

if llist.circularlinkedlist() == True:
    print("Circular Linked ")
else:
    print(0)


