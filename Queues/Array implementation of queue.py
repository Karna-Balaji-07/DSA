# Proram to implement queue using arrays

class Queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    # function to add element to the queue
    def Enqueue(self,item):
        if(self.isFull()):
            print("Overflow condition")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))

    def Dequeue(self):
        if self.isEmpty():
            print("underflow condition")
            return
        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1)  % self.capacity
        self.size = self.size -1

    def qfront(self):
        if self.isEmpty():
            print("Underflow")
            return
        return self.Q[self.front]

    def qrear(self):
        if self.isEmpty():
            print("Underflow")
            return
        return self.Q[self.rear]


queue = Queue(30)
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)
queue.Enqueue(50)
queue.Enqueue(60)
queue.Dequeue()
print(queue.qfront())
print(queue.qrear())
