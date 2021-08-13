'''
1. 부분집합을 범위 내에서 만들기..?
2. 인덱스에 따라서 따로따로 리스트에 append
3. 색별로 for문 돌면서 같은 좌표 나오면 ++
'''

T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 2차원 배열 행의 수 입력받기
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0 # 숫자 count
    red = [] # 빨간색 좌표
    blue = [] # 파란색 좌표
    for a in range(n):
        x1, y1, x2, y2, color = map(int, input().split())

        if color == 1: # 1이면 빨간색 리스트에 더하기
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    red.append([i, j])
        if color == 2: # 2 이면 파란색 리스트에 더하기
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    blue.append([i, j])

    # 색 리스트끼리 비교하여 같으면 count
    for r in red:
        for b in blue:
            if r == b:
                cnt += 1
    print(f'#{tc} {cnt}')



