T = int(input())

for t in range(1, T + 1):
    n = int(input())
    v = 0
    d = 0
    for _ in range(n):
        inputs = list(map(int, input().split()))
        if inputs[0] == 0:
            d += v
        elif inputs[0] == 1:
            v += inputs[1]
            d += v
        else:
            if v - inputs[1] < 0:
                v = 0
            else:
                v -= inputs[1]
            d += v
    print(f"#{t} {d}")

