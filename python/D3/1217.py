T = 10

for t in range(1, T + 1):
    tc = int(input())
    n, m = map(int, input().split())

    print(f"#{tc} {n ** m}")

