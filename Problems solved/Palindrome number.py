# Palindrome number

def palindrome1(n):
    if n < 0:
        return False
    rev = 0
    num = n
    while n > 0:
        temp = n %10
        n //= 10
        rev = (rev*10) + temp

    return rev == num


def palindrome2(n):
    if n<0 or (n !=0 and n%10 == 0):
        return False

    reversed = 0
    temp = n
    while n > reversed:
        reversed = (reversed * 10) + n %10
        n //= 10

    return n == reversed or n == reversed//10


n = 121
print(palindrome1(n))
print(palindrome2(n))
n = -121
print(palindrome1(n))
print(palindrome2(n))
n = 122121
print(palindrome1(n))
print(palindrome2(n))

