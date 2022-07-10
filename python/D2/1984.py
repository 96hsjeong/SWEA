T = int(input())

for t in range(1, T + 1):
    data = list(map(int, input().split()))
    min_ = min(data)
    max_ = max(data)
    while min_ in data:
        data.remove(min_)
    while max_ in data:
        data.remove(max_)
    answer = round(sum(data) / len(data))
    print(f"#{t} {answer}")