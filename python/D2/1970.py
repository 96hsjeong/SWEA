T = int(input())

for t in range(1, T + 1):
    n = int(input())
    money_type = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_cnt = [0] * len(money_type)

    for i in range(len(money_type)):
        money_cnt[i] = n // money_type[i]
        n %= money_type[i]

    print(f"#{t}")
    print(*money_cnt)