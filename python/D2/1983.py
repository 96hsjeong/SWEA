T = int(input())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    data = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(1, n + 1):
        mid, final, assignment = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + assignment * 0.2
        data.append((i, total))
        data.sort(key=lambda x: -x[1])
    for i in range(n):
        if data[i][0] == k:
            print(f"#{t} {grade[i//(n//10)]}")
            break