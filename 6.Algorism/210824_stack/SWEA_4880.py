'''
토너먼트
1 < 2 가위 < 바위
3 < 1  보 < 가위
2 < 3  바위 < 보
'''

def tnm(i, j): # 시작점, 끝점
    if i == j: # 한명 남으면
        return i # 대결할 사람이 결정됨
    else: # 대결할 사람 정하기
        r1 = tnm(i, (i+j)//2)  # 계속 r1으로 돔...
        # i, j = 0, n-1
        r2 = tnm((i+j)//2+1, j) # 기준으로 오른쪽부터
        # 가위 - 바위, 보
        if lst[r1] == lst[r2]:
            return r1 # 비겼을때 먼저 검사해서 아무거나 올려주기
        elif lst[r1] == 1:
            if lst[r2] == 2:
                return r2
            elif lst[r2] == 3:
                return r1
        # 바위 - 가위, 보
        elif lst[r1] == 2:
            if lst[r2] == 1:
                return r1
            elif lst[r2] == 3:
                return r2
        elif lst[r1] == 3:
            if lst[r2] == 1:
                return r2
            elif lst[r2] == 2:
                return r1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    print(f'#{tc} {tnm(0, n-1)+1}') # 인덱스로 접근해서 +1 해야함