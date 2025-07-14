def palindromeIndex(s):
    n = len(s)
    if s == s[::-1]:
        return -1
    for i,item in enumerate(s):
        s1 = s[(i+1):]
        s2 = s[:(n-1-i)]
        print(s1, 'its reverse ', s1[::-1])
        if(s1 == s1[::-1]):
            return i
        elif (s2 == s2[::-1]):
            return (n-1-i)
        else:
            return -1


s = 'aaab'
result = palindromeIndex(s)
print(s, result)