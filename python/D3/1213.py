for _ in range(10):
    tc = int(input())
    search = input()
    s = input()
    answer = 0

    for i in range(len(s) - len(search) + 1):
        if s[i: i + len(search)] == search:
            answer += 1

    print(f"#{tc} {answer}")



