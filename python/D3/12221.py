T = int(input())

for t in range(1, T + 1):
    A, B = map(int, input().split())
    answer = -1
    if 1 <= A <= 9 and 1 <= B <= 9:
        answer = A * B
    print(f"#{t} {answer}")