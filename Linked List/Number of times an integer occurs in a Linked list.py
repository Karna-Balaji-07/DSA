# To count the number of times a given integer occurs in a given linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlinkedlist(self):
        temp = self.head
        L = []
        while temp:
            L.append(temp.data)
            temp = temp.next
        return L

    def countelement(self,element):
        temp = self.head
        count = 0
        while temp:
            if temp.data == element:
                count += 1
            temp = temp.next

        return count

list = LinkedList()
list.push(1)
list.push(2)
list.push(1)
list.push(4)
list.push(10)
list.push(1)
list.push(1)
list.push(6)
list.push(1)
list.push(10)
list.push(1)
list.push(1)
list.push(10)


linkedlist = list.printlinkedlist()
print(linkedlist)

counting = list.countelement(1)
print(counting)
print()
counting = list.countelement(10)
print(counting)
