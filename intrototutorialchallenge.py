def introTutorial(V, arr):
    return arr.index(V)
V = int(input().strip())
n = int(input().strip())
arr = list(map(int, input().strip().split()))
result = introTutorial(V, arr)
print(result)