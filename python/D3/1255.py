from collections import deque

try:
    while True:
        tc = int(input())
        arr = deque(map(int, input().split()))

        x = -1
        k = 1

        while x != 0:
            x = arr.popleft()
            x -= k
            if x < 0:
                x = 0
            arr.append(x)
            k += 1
            if k > 5:
                k = 1


        print(f"#{tc}", *arr)
except:
    pass