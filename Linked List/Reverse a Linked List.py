# Reverse a linked list

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


list = LinkedList()
list.push(5)
list.push(4)
list.push(3)
list.push(2)
list.push(1)

print("Original Linked list : ")
list.printlist()
print(" ")
print("Reversed linked list ")
list.reverse()
list.printlist()