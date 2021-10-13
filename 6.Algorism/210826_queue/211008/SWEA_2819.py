'''
격자판의 숫자 이어 붙이기

- 격자판의 각 격자에는 0부터 9 사이의 숫자가 적혀있다.
- 임의의 위치 시작 + 동서남북 4방향(6자리) = 7자리의 수

- di, dj 의 수가 담긴 리스트 만들기
- 리스트에 담긴 수들로 6자리가 나오는 순열 생성
- 시작 위치 + 순열 해서 새로운 res 에 담기.
    if not res: res.append(tmp)



'''
# 상우좌하 순
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def DFS(r, c, line):
    if len(line) == 7:   # 7자리수 완성ㅇ
        ans.add(line)
        # if line not in ans:
        #     ans.append(line)
        # return
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4: continue
        DFS(nr, nc, line+arr[nr][nc])  # 이동한 위치를 넘겨줘서, 여기에서 인접한것 모두 탐색하게 된다.

# string 으로 넘겨줘야 한다. 현재 위치에서 + 연산으로 line을 구하기 때문
for tc in range(1, int(input())+1):
    arr = [input().split() for _ in range(4)]
    ans = set()  # 전체 일곱자리 수 담기
    for i in range(4):
        for j in range(4):
            DFS(i, j, arr[i][j])  # 현재위치값 넘겨주고  + 연산해서 확인하기

    print(f'#{tc} {len(ans)}')