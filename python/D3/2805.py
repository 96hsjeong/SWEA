T = int(input())

for t in range(1, T + 1):
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, list(input()))))

    x = n // 2
    k = 0

    answer = 0

    for i in range(n):
        answer += sum(arr[i][x - k: x + k + 1])
        if i < x:
            k += 1
        else:
            k -= 1

    print(f"#{t} {answer}")
