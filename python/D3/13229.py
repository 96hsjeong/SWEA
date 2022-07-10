T = int(input())

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for t in range(1, T + 1):
    S = input()
    answer = 7 - day.index(S)
    print(f"#{t} {answer}")

