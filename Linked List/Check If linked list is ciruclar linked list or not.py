# to check whether the given linked list is circular linked list or not

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        L = []
        while temp:
            L.append(temp.data)
            temp = temp.next
        return L

    def circular(self):
        if self.head is None:  # empty Linked list is also a circular linked list
            return True

        node = self.head.next
        i = 0
        while(node is not None) and (node is not self.head):
            i += 1
            node = node.next

        return node == self.head


list = LinkedList()
list.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

list.head.next = second
second.next = third
third.next = fourth

if (list.circular() == True):
    print("It is Circular linked List")
else:
    print("It is not a Circular Linked List")

fourth.next = list.head
if(list.circular()==True):
    print("It is a circular linked list")
else:
    print("It is not a circular linked list")