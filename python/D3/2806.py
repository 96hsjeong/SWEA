def check(q):
    for i in range(q):
        if queen[q] == queen[i] or abs(queen[q] - queen[i]) == q - i:
            return False
    return True

def dfs(x):
    global answer

    if x == n:
        answer += 1
    else:
        for i in range(n):
            queen[x] = i
            if check(x):
                dfs(x + 1)

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    queen = [0] * n
    answer = 0
    dfs(0)
    print(f"#{t} {answer}")