'''
최소 생산비용
각 공장 -> 열
비용 -> 행
n 종의 제품을 n곳에서 각 1개씩 생산 -> 최소값을 구하시오
'''

def cost(i, res):
    global minV
    if i == n: # 하나의 순열 완성
        minV = min(minV, res)
        return res
    elif res > minV:  # 백트래킹 조건 추가
        return
    else:
        for j in range(n):
            if visited[j]: continue   # 1로 표시되어있으면 해당하는 열 선택 안하도록 통과
            visited[j] = 1
            cost(i+1, res+lst[i][j])  # 재귀 호출할때에 비용 추가해서 넘겨주기
            visited[j] = 0            # 원상복구 해서 다음 경우에 선택할 수 있도록

for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    minV = 100*n
    cost(0, 0)   # 처음 인덱스가 0, 최소 생산 비용을 합칠 res 변수도 0.
    print(f'#{tc} {minV}')