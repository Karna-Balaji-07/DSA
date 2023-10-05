# Longest Palindromic substring

def substring(s):
    palindrome = ""
    if len(s) == 1:
        return s
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                if len(substring) > len(palindrome):
                    palindrome = substring
    return palindrome

s = "babad"
print(substring(s))