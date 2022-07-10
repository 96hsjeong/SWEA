from itertools import combinations

T = int(input())

for t in range(1, T + 1):
    N = list(input())
    target = [i for i in range(len(N))]
    min_val, max_val = int(''.join(N)), int(''.join(N))

    for i, j in combinations(target, 2):
        x = N[:]
        x[i], x[j] = x[j], x[i]
        if x[0] == 0:
            continue
        if int(''.join(x)) < min_val:
            min_val = int(''.join(x))
        if int(''.join(x)) > max_val:
            max_val = int(''.join(x))

    print(f"#{t} {min_val} {max_val}")
