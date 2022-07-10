T = int(input())

for t in range(1, T + 1):
    S = list(input())
    x = S.count('x')
    answer = 'YES'
    if x > 7:
        answer = 'NO'
    print(f"#{t} {answer}")