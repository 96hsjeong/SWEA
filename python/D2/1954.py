T = int(input())

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    x, y = 0, 0
    d = 0
    num = 1

    while num <= (n * n):
        arr[x][y] = num

        x += dx[d]
        y += dy[d]

        if x < 0 or y < 0 or x >= n or y >= n or arr[x][y] != 0:
            x -= dx[d]
            y -= dy[d]

            d = (d + 1) % 4

            x += dx[d]
            y += dy[d]

        num += 1

    print(f"#{t}")
    for i in range(n):
        print(*arr[i])
