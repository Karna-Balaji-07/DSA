# program to check for balanced brackets

def balanced(exp):
    stack = []
    for i in exp:
        if i in ["[","{","("]:
            stack.append(i)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char =="(":
                if i != ")":
                    return False
            if current_char == "{":
                if i != "}":
                    return False
            if current_char == "[":
                if i != "]":
                    return  False

    if stack:          # to check if the stack is empty
        return False
    return True

exp = "{}{}[]()(())"
if(balanced(exp)):
    print("Balanced")
else:
    print("Not Balanced")

