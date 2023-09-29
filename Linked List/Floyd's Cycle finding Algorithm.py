# Floyd's Cycle finding algorithm / hare-tortoise algorithm

# Floyd’s cycle finding algorithm or Hare-Tortoise algorithm is a pointer algorithm that uses only two pointers, moving through the sequence at different speeds. This algorithm is used to find a loop in a linked list. It uses two pointers one moving twice as fast as the other one. The faster one is called the fast pointer and the other one is called the slow pointer.

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next= None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self,newdata):
#         newNode = Node(newdata)
#         newNode.next = self.head
#         self.head = newNode
#
#     def detectloop(self):
#         slowpointer = self.head
#         fastpointer = self.head
#         while slowpointer is not None and fastpointer is not None and fastpointer.next is not None:
#             slowpointer = slowpointer.next
#             fastpointer = fastpointer.next.next
#             if slowpointer == fastpointer:
#                 return True
#         return False
#
#
#
#     def printlist(self):
#         temp = self.head
#         L = []
#         while temp:
#             L.append(temp.data)
#             temp = temp.next
#         return L
#
#
# list = LinkedList()
# head = None
# list.push(60)
# list.push(50)
# list.push(40)
# list.push(30)
# list.push(20)
# list.push(10)
# res = list.printlist()
# print(res)
# print()
# # list.head.next.next.next.next.next = list.head.next.next.next
# if list.detectloop():
#     print(True)
# else:
#     print(False)
#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

    def detectloop(self):
        slowpointer = self.head
        fastpointer = self.head
        while slowpointer is not None and fastpointer is not None and fastpointer.next is not None:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next
            if slowpointer == fastpointer:
                break
        if slowpointer != fastpointer:
            return None

        slowpointer = self.head
        while slowpointer != fastpointer:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next
        return slowpointer


    def printlist(self):
        temp = self.head
        L = []
        while temp:
            L.append(temp.data)
            temp = temp.next
        return L


list = LinkedList()
head = None
n = int(input())
for i in range(n):
    x = int(input())
    list.push(x)
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
loopstart = list.detectloop()
if loopstart is None:
    print("Loop does not exists")
else:
    print(f'Loop does exists and starts at {loopstart.data}')


