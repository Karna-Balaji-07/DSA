#Linked list Operations
# Searching an element in linked list using iterative approach

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node  = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self,key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False



llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.push(60)

key = 30

if llist.search(key):
    print("YES")
else:
    print("NO")