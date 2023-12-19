def separateNumbers(s):
    n = len(s)
    for i in range(1, n//2 + 1):
        x = int(s[:i])
        current = x
        answer = str(x)
        while len(answer) < n:
            current += 1
            answer += str(current)
        if answer == s:
            print(f"YES {x}")
    print("NO")
n = int(input())
s = input()
result = separateNumbers(s)
print(result)