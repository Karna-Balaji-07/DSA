# Insertion in a linked List

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data);
        new_node.next = self.head
        self.head = new_node

    def InsertFront(self, new_data):
        new_node = Node(new_data);
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        res = []
        while (temp):
            res.append(temp.data)
            temp = temp.next
        return res


list = LinkedList()
list.push(5)
list.push(4)
list.push(3)
list.push(2)
list.push(1)

print(list.printlist())
list.InsertFront(10)
print(list.printlist())
