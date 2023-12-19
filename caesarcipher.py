def caesarCipher(s, k):
    result = ""
    for char in s:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + k) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char
    return result
n = int(input().strip())
s = input().strip()
k = int(input().strip())
result = caesarCipher(s, k)
print(result)