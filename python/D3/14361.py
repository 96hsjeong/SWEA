T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, str(N)))
    nums.sort()

    answer = 'impossible'

    k = 2
    while len(str(k * N)) <= len(nums):
        x = list(map(int, str(k * N)))
        x.sort()
        if nums == x:
            answer = 'possible'
        k += 1

    print(f"#{t} {answer}")

