'''
요리사
n 개의 조합 만들어서 조합 앞뒤 바꿔서 계산

'''
from itertools import combinations

for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    R = n//2

    minV = 2000*n**2

    # 조합을 따로 구해서 돌리면 runtime error.
    for ar in combinations(range(n), R):
        arr = []  # 맨 처음 만든 조합과 겹치지 않는 값들(둘로 나뉠 수 있는 재료 종류)
        for j in range(n):
            if j not in ar:
                arr.append(j)
        tmp1 = 0
        tmp2 = 0
        # arr의 조합에서 다시 조합을 만들어서 tmp에 더하기. 겹치지 않도록 r+1로 for 문 돌리기
        for r in range(R-1):
            for c in range(r+1, R):
                tmp1 += lst[ar[r]][ar[c]] + lst[ar[c]][ar[r]]
                tmp2 += lst[arr[r]][arr[c]] + lst[arr[c]][arr[r]]
        minV = min(minV, abs(tmp1-tmp2))

    print(f'#{tc} {minV}')
