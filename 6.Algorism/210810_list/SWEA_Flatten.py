'''
1. 총 상자를 옮기는 횟수 = move
2. 입력 받은 리스트 = box
3. box 리스트의 maxb 를 구하고
4. box 리스트의 minb 를  구한다.
5. maxb -1, minb +1 을 하면 총 1번의 이동
6. 이동할때마다 move--
7. 문제는 이동한 이후의 리스트를 어떻게 처리할것인가...?
8. 최대값의 인덱스를 찾기
9. 그 최대값의 인덱스에 + - 1 한 값을 재할당.
'''

for tc in range(10):
    result = 0
    moves = int(input())
    a_list = list(map(int, input().split()))
    while moves > 0:
        max_v = 0
        min_v = 101
        max_idx = -1
        min_idx = -1
        # 가장 높은 곳의 인덱스와 값 구하기
        for i, v in enumerate(a_list):
            if max_v < v:
                max_v = v
                max_idx = i
        a_list[max_idx] = (max_v - 1)  # 높은곳인덱스의 값 -1
        # 가장 낮은 곳의 인덱스와 값 구하기
        for i, v in enumerate(a_list):
            if min_v > v:
                min_v = v
                min_idx = i
        a_list[min_idx] = (min_v + 1)  # 낮은곳 인덱스의 값 +1

        moves -= 1
        result = max(a_list) - min(a_list)
    print(f'#{tc+1} {result}')

'''
for t in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(99, 0, -1):                    # 버블 정렬
        for j in range(i):
            if box[j] > box[j + 1]:
                box[j], box[j + 1] = box[j + 1], box[j]
 
    for d in range(dump):
        box[0] += 1                               # 더하기 1, 빼기 1 해주고
        box[-1] -= 1
        for i in range(100):                      # 다시 정렬해줌
            if box[i] > box[i+1]:
                box[i], box[i+1] = box[i+1], box[i]
            else:
                break
        for i in range(-1, -101, -1):
            if box[i-1] > box[i]:
                box[i], box[i-1] = box[i-1], box[i]
            else:
                break
 
        if box[-1] - box[0] <= 1:
            break
    print('#{} {}'.format(t+1, box[-1] - box[0]))
'''