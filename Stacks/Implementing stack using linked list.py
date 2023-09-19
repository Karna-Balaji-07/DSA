# Implementing stacks using singly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head is None else False

    def push(self,newdata):
        newnode = Node(newdata)
        newnode.next= self.head
        self.head = newnode
        print("%d pushed into stack" % newdata)

    def pop(self):
        if(self.isEmpty()):
            return -1
        temp = self.head
        self.head = self.head.next
        popped = temp.data
        return popped

    def peek(self):
        if(self.isEmpty()):
            return -1
        return self.head.data


    def printlsit(self):
        temp = self.head
        if(self.isEmpty()):
            return -1
        L = []
        while temp:
            L.append(temp.data)
            temp = temp.next
        return L




stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
res = stack.printlsit()
print(res)

print("%d popped fromm the stack"%stack.pop())
print((stack.printlsit()))

print("%d is the top or last added element"%stack.peek())

