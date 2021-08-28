'''
토너먼트
1 < 2 가위 < 바위
3 < 1  보 < 가위
2 < 3  바위 < 보
'''
def tnm(i, j): # 시작점, 끝점
    if i == j: # 한명 남으면
        return lst[i] # 대결할 사람 결정됨

    elif i !=j:
        r1 = tnm(i, (i+j)//2)
        if r1:
            i, j = 0, n-1
            r2 = tnm((i+j)//2, j)
        # 가위 - 바위, 보
        if lst[r1] == 1:
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
                return r1
            elif lst[r2] == 2:
                return r1


n = int(input())
lst = list(map(int, input().split()))
tnm(0, n-1) # 시작의 양 끝