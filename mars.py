def mars(s):
    msg = "SOS"
    change = 0
    for i in range(len(s)):
        if s[i]!=msg[i%3]:
            change+=1
    return change
s=input()
output = mars(s)
print(output)