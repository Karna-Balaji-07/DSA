# Implementing stacks using arrays

def createtack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0
def push(stack,item):
    stack.append(item)
    print(f'{item} pushed into stack')

def printstack(stack):
    return stack

def pop(stack):
    if isEmpty(stack):
        print(-1)
    stack.pop()

def top(stack):
    if isEmpty(stack):
        print(-1)
    return stack[len(stack)-1]

stacks = createtack()
push(stacks,10)
push(stacks,20)
push(stacks,30)
push(stacks,40)
push(stacks,50)
res = printstack(stacks)
print(res)

pop(stacks)
res = printstack(stacks)
print(res)



