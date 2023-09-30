# program to convert prefix expression to infix expression

def Conversion(exp):
    stacks= []
    i = len(exp) - 1
    while i >= 0:
        if not isOperator(exp[i]):
            stacks.append(exp[i])
            i -= 1
        else:
            str = "(" + stacks.pop() + exp[i] + stacks.pop() + ")"
            stacks.append(str)
            i -= 1
    return stacks.pop()

def isOperator(c):
    if c=="*" or c=="+" or c=="-" or c=="/" or c=="(" or c == ")":
        return True
    else:
        return False

str = "*-A/BC-/AKL"
x = Conversion(str)
print(x)