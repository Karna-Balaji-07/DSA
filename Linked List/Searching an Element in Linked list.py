#Linked list ooperations
# Searching an element in linked list using 0(N) extra space

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

linkedlist = LinkedList()
linkedlist.push(10)
linkedlist.push(20)
linkedlist.push(30)
linkedlist.push(40)
linkedlist.push(50)

x = 30
L = []
temp = linkedlist.head
while(temp):
    L.append(temp.data)
    temp = temp.next

if x in L:
    print("YEs")
else:
    print("NO")