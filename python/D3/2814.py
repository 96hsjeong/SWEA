def dfs(idx, ans):
    global answer

    ans += 1
    visited[idx] = 1

    if answer < ans:
        answer = ans

    for i in graph[idx]:
        if not visited[i]:
            dfs(i, ans)

    visited[idx] = 0

T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [0] * (n + 1)
    answer = 0

    for i in range(n):
        dfs(i, 0)

    print(f"#{t} {answer}")

