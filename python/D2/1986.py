def solution(n):
    if n % 2 == 0:
        answer = -(n // 2)
    else:
        answer = n - ((n - 1) // 2)
    return answer

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    print(f"#{t} {solution(n)}")