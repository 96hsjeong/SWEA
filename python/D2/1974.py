T = int(input())

for t in range(1, T + 1):
    matrix = [[0] * 9 for _ in range(9)]
    matrix_t = [[0] * 9 for _ in range(9)]
    grid = [[0] * 3 for _ in range(3)]

    test = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    test_grid = [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
    answer = 1

    for i in range(9):
        data = list(map(int, input().split()))
        for j in range(9):
            matrix[i][j] = data[j]
            matrix_t[j][i] = data[j]
            grid[i//3][j//3] += data[j]


    for i in range(9):
        if set(matrix[i]) != test or set(matrix_t[i]) != test:
            answer = 0
            break

    if test_grid != grid:
        answer = 0

    print(f"#{t} {answer}")