T = 10

for t in range(1, T + 1):
    tc = int(input())
    arr = []

    row = []
    col = [0] * 100
    lr = 0
    rl = 0
    answer = 0

    for _ in range(100):
        arr.append(list(map(int, input().split())))
    for i in range(100):
        row.append(sum(arr[i]))
        for j in range(100):
            if i == j:
                lr += arr[i][j]
            if i + j == 99:
                rl += arr[i][j]
            col[j] += arr[i][j]

    answer = max(max(row), max(col), lr, rl)

    print(f"#{tc} {answer}")




