def twoStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    common_chars = set1.intersection(set2)
    return "YES" if common_chars else "NO"
t = int(input().strip())
for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)