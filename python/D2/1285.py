T = int(input())

for t in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    min_distance = 999999
    min_count = 0

    for i in data:
        if min_distance > abs(i):
            min_distance = abs(i)
            min_count = 1
        elif min_distance == abs(i):
            min_count += 1
        else:
            continue

    print(f"#{t} {min_distance} {min_count}")
