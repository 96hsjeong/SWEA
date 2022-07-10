T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())

    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    max_die = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            die = 0
            for k in range(m):
                die += sum(data[i+k][j:j+m])
            max_die = max(max_die, die)

    print(f"#{t} {max_die}")
