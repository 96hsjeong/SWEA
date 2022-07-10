def isPalindrome(s):
    return s == s[::-1]

T = 10

for t in range(1, T + 1):
    p_len = int(input())

    arr = []
    arr_T = []
    answer = 0

    for _ in range(8):
        arr.append(list(input()))

    arr_T = [list(x) for x in zip(*arr)]

    for i in range(8):
        for j in range(8 - p_len + 1):
            if isPalindrome(arr[i][j: j + p_len]):
                answer += 1
            if isPalindrome(arr_T[i][j: j + p_len]):
                answer += 1

    print(f"#{t} {answer}")