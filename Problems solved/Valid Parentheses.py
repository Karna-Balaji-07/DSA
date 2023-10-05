# valid parentheses

def valid(s):
    stack = []
    for i in s:
        if i in ['(','{','[']:
            stack.append(i)
        else:
            if not stack:
                return False
            current = stack.pop()
            if current == '(':
                if i != ')':
                    return False
            if current == '{':
                if i != '}':
                    return False
            if current == '[':
                if i != ']':
                    return False
    if stack:
        return False
    return True

s = "{}()[]"
print(valid(s))

