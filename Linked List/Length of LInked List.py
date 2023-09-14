# To find the length of the linked list/ to count the number of nodes in a linked list

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

    def counter(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count


llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.push(60)

print(f'Number of nodes in the linked list is {llist.counter()}')
