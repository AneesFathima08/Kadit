def runningTime(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = key
    return shifts
n = int(input().strip())
arr = list(map(int, input().strip().split()))
result = runningTime(arr)
print(result)