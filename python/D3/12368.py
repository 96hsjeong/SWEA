T = int(input())

for t in range(1, T + 1):
    A, B = map(int, input().split())
    answer = A + B
    if answer >= 24:
        answer -= 24
    print(f"#{t} {answer}")