# To find the length of the linked list using FLoyd's cycle algorithm

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

    def detectloop(self):
        slowpointer = self.head
        fastpointer = self.head
        flag = 0
        while slowpointer and slowpointer.next and fastpointer and fastpointer.next and fastpointer.next.next:

            if slowpointer == fastpointer and flag != 0:
                count = 1
                slowpointer = slowpointer.next
                while slowpointer != fastpointer:
                    slowpointer = slowpointer.next
                    count += 1
                return count
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next
            flag = 1

    def printlist(self):
        temp = self.head
        L = []
        while temp:
            L.append(temp.data)
            temp = temp.next
        return L


list = LinkedList()
head = None
list.push(60)
list.push(50)
list.push(40)
list.push(30)
list.push(20)
list.push(10)
res = list.printlist()
print(res)
print()
list.head.next.next.next.next.next = list.head.next.next
looplength = list.detectloop()
print(looplength)