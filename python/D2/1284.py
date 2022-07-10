T = int(input())

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    B = 0

    if W <= R:
        B = Q
    else:
        B = Q + S * (W - R)

    answer = A if A < B else B
    print(f"#{t} {answer}")