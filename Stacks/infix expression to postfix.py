# program to convert infix expression to postfix expression

class Conversion:
    def __init__(self,capacity):    # constructor to initialie the variable
        self.top = -1
        self.capacity = capacity
        self.array = []   # stack
        self.outing = []   #precedence setting
        self.precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}


    # To check if the stack is empty or not
    def isempty(self):
        return True if self.top == -1 else False

    # Return the value of the top element
    def peek(self):
        return self.array[-1]

    # pop element from the stack
    def pop(self):
        if not self.isempty():
            self.top -=1
            return self.array.pop()
        else:
            return '$'

    # push the element in the stack
    def push(self,op):
        self.top += 1
        self.array.append(op)

    # to check if the given character is operand
    def isoperand(self,ch):
        return ch.isalpha()

    # fucntion to check if the precedence of the operator is strictly less than the top of the stack
    def notGreater(self,i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False

    # infix to postfix conversion
    def infixtopostfix(self,exp):
        for i in exp:       # iterate over the expression
            if self.isoperand(i):
                self.outing.append(i)


            elif i == '(':      # if the character is '(' add it to the stack
                self.push(i)

            elif i == ')':  # if the scanned operator is ')' pop and output from the stack untill '(' is found
                while(not self.isempty()) and self.peek() != '(':
                    a = self.pop()
                    self.outing.append(a)

                if not self.isempty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()

            # when operator is encountered
            else:
                while not self.isempty() and self.notGreater(i):
                    self.outing.append(self.pop())
                self.push(i)

        while not self.isempty():
            self.outing.append(self.pop())

        for ch in self.outing:
            print(ch, end=" ")



exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixtopostfix(exp)
