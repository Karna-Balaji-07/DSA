# count nodes in a circular linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        ptr = Node(data)
        ptr.next = self.head
        temp = self.head

        if self.head is not None:
            while temp != self.head:
                temp = temp.next
            temp.next= ptr
        else:
            ptr.next = ptr
        self.head = ptr

    def countnodes(self):
        count = 0
        if self.head is not None:
            temp = self.head
            while True:
                count += 1
                temp = temp.next
                if temp == self.head:
                    break
        return count


list = LinkedList()
list.push(10)
list.push(20)
list.push(30)
list.push(40)
list.push(50)
list.push(60)

list.head.next.next.next.next.next.next = list.head
res = list.countnodes()
print(res)
