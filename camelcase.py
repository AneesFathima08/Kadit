def camelcase(s):
    word_count = sum(1 for char in s if char.isupper()) + 1
    return word_count

s = input()
result = camelcase(s)
print(result)