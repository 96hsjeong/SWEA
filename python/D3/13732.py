T = int(input())

for t in range(1, T + 1):
    n = int(input())
    board = []
    x, y = -1, -1
    count = 0
    size = 0
    answer = 'yes'
    for i in range(n):
        board.append(list(input()))
        count += board[i].count('#')
        if '#' in board[i] and x == -1 and y == -1:
            x, y = i, board[i].index('#')
            size = board[i].count('#')

    if count != size * size:
        answer = 'no'
    else:
        for i in range(size):
            for j in range(size):
                if board[x + i][y + j] != '#':
                    answer = 'no'
                    break
            if answer == 'no':
                break

    print(f"#{t} {answer}")



