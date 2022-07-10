def char2num(x):
    if x.isalpha():
        if x.isupper():
            n = ord(x) - 65
        else:
            n = ord(x) - 71
    else:
        if x.isnumeric():
            n = ord(x) + 4
        elif x == '+':
            n = ord(x) + 19
        elif x == '/':
            n = ord(x) + 16
    return n


def num2bit(n):
    buffer = []
    while len(buffer) < 6:
        buffer.append(n % 2)
        n //= 2
    buffer.reverse()
    return buffer


def byte2num(buffer):
    num = 0
    buffer.reverse()
    for i in range(8):
        num += buffer[i] * pow(2, i)
    return num


def decoding(s):
    answer = ''
    for i in range(len(s) // 4):
        x = s[i * 4: i * 4 + 4]
        buffer = []
        for c in x:
            n = char2num(c)
            buffer.extend(num2bit(n))
        for j in range(3):
            n = byte2num(buffer[j * 8: j * 8 + 8])
            answer += chr(n)
    return answer


T = int(input())

for t in range(1, T + 1):
    s = input()
    answer = decoding(s)
    print(f"#{t} {answer}")
