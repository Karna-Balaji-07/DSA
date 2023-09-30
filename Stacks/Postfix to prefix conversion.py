# Program to convert postfix expression to prefix expression

def isOperator(x):
    if x == '+' or x == '-' or x == '*' or x == '/' :
        return True
    else:
        return False

def Conversion(exp):
    length = len(exp)
    stack = []
    for i in range(length):
        if isOperator(exp[i]):
            op1 = stack[-1]
            stack.pop()
            op2 = stack[-1]
            stack.pop()
            temp = exp[i] + op2 + op1
            stack.append(temp)

        else:
            stack.append(exp[i])

    ans = ""
    for i in stack:
        ans += i
    return ans


exp = "AB+CD-"
print(Conversion(exp))