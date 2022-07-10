prime = [2, 3, 5, 7, 11]

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    answer = [0] * 5

    for i in range(len(prime)):
        while True:
            if n % prime[i] == 0:
                n //= prime[i]
                answer[i] += 1
            else:
                break
    print(f"#{t}", end=' ')
    print(*answer)