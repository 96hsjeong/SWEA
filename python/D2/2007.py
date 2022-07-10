T = int(input())

for t in range(1, T + 1):
    case = input()
    for i in range(1, 11):
        found = True
        keyword = case[0: i]
        start = i
        while start < 30 - i:
            k = case[start: start + i]
            if keyword == k:
                start += i
            else:
                found = False
                break

        if found:
            print(f"#{t} {len(keyword)}")
            break