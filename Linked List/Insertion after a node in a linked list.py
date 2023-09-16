# inserting node after a given node in a linked list

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

    def insertafter(self,previous,new_data):
        if previous is None:
            print("Previous Node is NULL ")
            return
        new_node = Node(new_data)
        new_node.next = previous.next
        previous.next = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

list = LinkedList()
list.push(6)
list.push(5)
list.push(3)
list.push(2)
list.push(1)

print(list.printlist())
list.insertafter(list.head,10)
print(list.printlist())
list.insertafter(list.head.next.next,50)
print((list.printlist()))