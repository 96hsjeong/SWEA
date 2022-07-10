T = int(input())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    answer = 0
    puzzle = []
    for _ in range(n):
        puzzle.append(list(map(int, input().split())))

    for r in range(n):
        cnt = 0
        for c in range(n):
            if puzzle[r][c] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:
            answer += 1

    for c in range(n):
        cnt = 0
        for r in range(n):
            if puzzle[r][c] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:
            answer += 1

    print(f"#{t} {answer}")
