T = int(input())

for t in range(1, T + 1):
    x = input()
    result = 1 if x == x[::-1] else 0
    print(f"#{t} {result}")