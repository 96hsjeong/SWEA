T = 10

for t in range(1, T + 1):
    count = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(count):
        M_idx = boxes.index(max(boxes))
        m_idx = boxes.index(min(boxes))
        boxes[M_idx] -= 1
        boxes[m_idx] += 1

    print(f"#{t} {max(boxes) - min(boxes)}")