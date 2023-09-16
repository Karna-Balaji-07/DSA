# program to traverse the circular linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head= new_node

        # Function to print nodes in a given circular linked list
        def printList(self):
            temp = self.head
            if self.head is not None:
                while (True):
                    print(temp.data, end=" ")
                    temp = temp.next
                    if (temp == self.head):
                        break

    # Driver program to test above function

    # Initialize list as empty
cllist = LinkedList()

    # Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)

print("Contents of circular Linked List")
cllist.printList()