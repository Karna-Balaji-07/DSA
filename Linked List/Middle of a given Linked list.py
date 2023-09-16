# Find the middle of the given linked list
#
# if the given linked list is 1->2->3->4->5 then the output should be 3.
# If there are even nodes, then there would be two middle nodes, we need to print the second middle element.
# For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4.


class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.next
        return count

    def middleelement(self):
        if self.head is not None:
            count = self.length()
            temp = self.head

            middle = count//2
            while middle!=0:
                temp = temp.next
                middle -= 1
            print("Middle element is ",temp.data)


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


list = Linkedlist()
list.push(10)
list.push(20)
list.push(30)
list.push(40)
list.push(50)
list.push(60)
list.push(70)

list.printlist()
print(" ")
list.middleelement()

