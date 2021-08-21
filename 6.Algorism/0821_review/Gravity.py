
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    boxes = list(map(int, input().split()))
    # [7, 4, 2, 0, 0, 6, 0, 7, 0]

    total = []
    for i in range(len(boxes)):
        cnt = 0  # 낙차
        res = boxes[i]
        for j in range(i+1, len(boxes)):
            if res > boxes[j]:
                cnt += 1
        total.append(cnt)
    print(f'#{tc} {max(total)}')
