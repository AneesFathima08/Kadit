def hackerrankInString(s):
    target = "hackerrank"
    pos = 0
    for char in s:
        if char == target[pos]:
            pos += 1
            if pos == len(target):
                return "YES"
    return "NO"
n = int(input())
s = input()
result = hackerrankInString(s)
print(result)