T = 10

for t in range(1, T + 1):
    n = int(input())
    tc = list(map(int, input().split()))

    count = 0

    i = 0
    while i < n:
        if tc[i] == 0:
            i += 1
            continue

        view = sorted(tc[i-2: i + 3])

        if view[-1] == tc[i]:
            count += tc[i] - view[-2]
            i += 3
        else:
            i += 1

    print(f"#{t} {count}")