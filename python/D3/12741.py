T = int(input())

result = []

for t in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    answer = 0

    answer = min(B, D) - max(A, C)
    answer = answer if answer > 0 else 0

    result.append(f"#{t} {answer}")

for r in result:
    print(r)