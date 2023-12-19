def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    has_number = False
    has_lower = False
    has_upper = False
    has_special = False

    for char in password:
        if char in numbers:
            has_number = True
        elif char in lower_case:
            has_lower = True
        elif char in upper_case:
            has_upper = True
        elif char in special_characters:
            has_special = True

    missing_types = 0
    if not has_number:
        missing_types += 1
    if not has_lower:
        missing_types += 1
    if not has_upper:
        missing_types += 1
    if not has_special:
        missing_types += 1

    total_characters_to_add = max(missing_types, 6 - n)

    return total_characters_to_add

n = int(input())
password = input().strip()
result = minimumNumber(n, password)
print(result)