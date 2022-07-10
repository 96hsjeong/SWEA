days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for t in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    d = 0

    if m1 == m2:
        d += d2 - d1 + 1
    else:
        for i in range(m1, m2):
            if i == m1:
                d += days[i] - d1 + 1
            else:
                d += days[i]
        d += d2

    print(f"#{t} {d}")

