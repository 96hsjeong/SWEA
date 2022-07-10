T = int(input())

for t in range(1, T + 1):
    n = int(input())
    nums = set()
    count = 0

    while len(nums) < 10:
        count += 1
        for i in str(n * count):
            nums.add(i)

    print(f"#{t} {count * n}")