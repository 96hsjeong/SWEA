T = int(input())

for t in range(1, T + 1):
    n = int(input())
    dp = [[0] * n for i in range(n)]
    print(f"#{t}")
    for i in range(n):
        dp[i][0] = 1
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        print(*dp[i][0:i+1])