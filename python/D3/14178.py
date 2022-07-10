import math

T = int(input())

for t in range(1, T + 1):
    N, D = map(int, input().split())
    answer = math.ceil(N / (2 * D + 1))
    print(f"#{t} {answer}")
