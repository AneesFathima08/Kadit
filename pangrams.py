def pangrams(s):
    s = s.lower()
    letters_set = set()
    for char in s:
        if char.isalpha():
            letters_set.add(char)
    if len(letters_set) == 26:
        return "pangram"
    else:
        return "not pangram"
s = input()
result = pangrams(s)
print(result)
