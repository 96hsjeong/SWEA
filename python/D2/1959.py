T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        A, B = B, A

    max_ = 0

    for i in range(m - n + 1):
        val = 0
        for j in range(n):
            val += A[j] * B[i+j]
        max_ = max(max_, val)

    print(f"{t} {max_}")
