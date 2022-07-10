def rotate90(arr):
    n = len(arr)
    arr90 = []
    for j in range(n):
        row = []
        for i in range(n - 1, -1, -1):
            row.append(arr[i][j])
        arr90.append(row)
    return arr90


T = int(input())

for t in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr90 = rotate90(arr)
    arr180 = rotate90(arr90)
    arr270 = rotate90(arr180)

    print(f"#{t}")
    for i in range(n):
        print(*arr90[i], sep='', end=' ')
        print(*arr180[i], sep='', end=' ')
        print(*arr270[i], sep='')
