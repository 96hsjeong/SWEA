T = int(input())

for t in range(1, T + 1):
    n = int(input())
    class_week = list(map(int, input().split()))

    class_cnt = class_week.count(1)

    day = 0

    if n == 1:
        day = 1
    elif n <= class_cnt:
        class_idx = []
        dist = []
        for i in range(7):
            if class_week[i] == 1:
                class_idx.append(i)

        dist = [class_idx[0] + 7 - class_idx[-1]]

        for i in range(len(class_idx) - 1):
            dist.append(class_idx[i + 1] - class_idx[i])
        min_dist = 9

        for i in range(class_cnt - n + 2):
            min_dist = min(min_dist, sum(dist[i: i + n - 1]))
        day = min_dist + 1
    elif n == class_cnt + 1:
        day = 8
    else:
        day += (n // class_cnt - 1) * 7
        r = n % class_cnt + class_cnt
        left_day, right_day = 0, 0
        left_cnt, right_cnt = 0, 0

        for i in range(7):
            min_day = min(left_day, right_day)
            if class_week[i] == 1:
                left_day = i + 1
                left_cnt += 1
            if class_week[6 - i] == 1:
                right_day = i + 1
                right_cnt += 1

            if left_cnt + right_cnt == r:
                day += left_day + right_day
                break
            elif left_cnt + right_cnt > r:
                day += min_day + left_day
                break

    print(f"#{t} {day}")