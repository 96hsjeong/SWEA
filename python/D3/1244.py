# fail

from itertools import combinations

T = int(input())

for t in range(1, T + 1):
    n, c = map(int, input().split())


    idxs = [i for i in range(len(str(n)))]

    max_val = 0

    for _ in range(c):
        for i, j in combinations(idxs, 2):
            x = list(str(n))
            x[i], x[j] = x[j], x[i]
            if int(''.join(x)) > max_val:
                max_val = int(''.join(x))
        print(max_val)
        n = max_val

    print(f"#{t} {n}")

