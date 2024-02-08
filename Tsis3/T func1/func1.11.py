def pol(s):
    j=len(s)
    for i in range(len(s)//2):
        if s[i]!=s[j-i-1]:
            print("Not polindrom")
            return 0
        
    print("Polindrom")
    return 0

s=input("Input:")
pol(s)