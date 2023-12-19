def bigSorting(num):
    num.sort(key=lambda x: (len(x), x))
    return num

n = int(input().strip())
num = [input().strip() for _ in range(n)]

result = bigSorting(num)
for value in result:
    print(value)