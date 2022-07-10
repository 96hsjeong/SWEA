T = int(input())

for t in range(1, T + 1):
    n = int(input())

    data = []
    start = 0

    print(f"#{t}")

    for _ in range(n):
        inputs = input().split()
        # alphabet.append(inputs[0])
        # count.append(int(inputs[1]))
        data.extend([inputs[0]] * int(inputs[1]))

    for _ in range(len(data) // 10):
        print(*data[start: start + 10], sep='')
        start += 10
        
    print(*data[start:], sep='')

