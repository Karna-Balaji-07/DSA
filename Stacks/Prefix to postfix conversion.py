# program to convert prefix expression to postfix expression

def conversion(exp):
    stacks = []
    operators = {'+', '-', '*', '/', '^'}
    rev = exp[::-1]
    for i in rev:
        if i in operators:
            a = stacks.pop()
            b = stacks.pop()
            temp = a+b+i
            stacks.append(temp)
        else:
            stacks.append(i)

    return stacks

exp = "*-A/BC-/AKL"
print(conversion(exp))