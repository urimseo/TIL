'''
벽돌꺠기
- 구슬 n 번 떨어뜨리기
-> 모든 위치에서 떨어뜨려 보기
'''


def f(org, N, W, H):  # org 발사 전 벽돌 상태, N 남은 발사 횟수
    global minV
    if N == 0:  # 남은 발사횟수가 없으면 남은 벽돌 세기
        cnt = 0
        for i in range(H):
            for j in range(W):
                if org[i][j]:
                    cnt += 1
        if minV > cnt:
            minV = cnt
    else:  # 구슬을 발사할 수 있으면
        for k in range(W):  # k 구슬을 발사할 위치
            dest =  org[::]

            # 발사...
            r = 0
            while r < H and dest[r][k] == 0:  # 구슬을 발사한 위치의 맨 윗 벽돌 찾기
                r += 1
            if r < H:
                buf = [(r, k, dest[r][k])]  # 깨지는 벽돌
                dest[r][k] = 0
                while buf:
                    i, j, t = buf.pop(0)
                    for p in range(1, t):
                        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                            ni, nj = i + di * p, j + dj * p
                            if 0 <= ni < H and 0 <= nj < W and dest[ni][nj] > 0:
                                buf.append((ni, nj, dest[ni][nj]))
                                dest[ni][nj] = 0
                # 빈공간 제거
                for j in range(W):
                    s = []
                    for i in range(H - 1, -1, -1):
                        if dest[i][j]:
                            s.append(dest[i][j])
                            dest[i][j] = 0
                    for i in range(len(s)):
                        dest[H - 1 - i][j] = s[i]

            f(dest, N - 1, W, H)  # 다음 구슬 발사


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    minV = W * H  # 최소로 남은 벽돌
    f(A, N, W, H)  # 남은 발사 횟수
    print(f'#{tc} {minV}')