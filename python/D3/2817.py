from itertools import combinations

T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    answer = 0

    for i in range(1, len(A) + 1):

        for x in combinations(A, i):
            if m == sum(x):
                answer += 1

    print(f"#{t} {answer}")