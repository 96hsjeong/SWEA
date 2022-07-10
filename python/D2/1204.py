T = int(input())

for _ in range(1, T + 1):
    test_case = int(input())
    data_list = list(map(int, input().split()))
    count = [0] * 101
    for data in data_list:
        count[data] += 1
    max_count = max(count)
    for i in range(100, -1, -1):
        if count[i] == max_count:
            print(f"#{test_case} {i}")
            break