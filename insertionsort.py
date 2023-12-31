def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(" ".join(map(str, arr)))

n = int(input().strip())
arr = list(map(int, input().strip().split()))
insertionSort2(n, arr)