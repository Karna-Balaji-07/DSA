# program to convert postfix expressin to infix expression

def isOperand(c):
    if('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        return True
    else:
        return False

def Conversion(exp):
    stack = []
    for i in exp:
        if isOperand(i):
            stack.insert(0,i)
        else:
            op1 = stack[0]
            stack.pop(0)
            op2 = stack[0]
            stack.pop(0)
            stack.insert(0,"("+op2+i+op1+")")

    return stack[0]

exp = "ab*c+"
print(Conversion(exp))
