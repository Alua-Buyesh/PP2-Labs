def palindrome(s):
    return s == s[::-1]

s=["20002","6767","9999","aba","uygkjhbn"]
for i in s:
    if palindrome(i):
        print("Palindrome")
    else:
        print("Not a palindrome")