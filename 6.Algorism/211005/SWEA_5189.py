'''
전기카트
- 사무실에서 출발해 각 구역을 한번씩만 방문하고 사무실로 돌아올 떄의 최소 배터리 사용량

1. 순열을 완성한 후에 비용계산
2. 다음 방문지를 결정 하는 순간 비용 결정

'''

def f(i, k):
    if i == k:  # 경로 한개 완성
        s = bat[0][A[0]]  # 사무실 -> 첫 경유지 가는데 드는 배터리 소비량
        for j in range(k-1):  # 경유지의 출발 인덱스        # 경유지 사이의 비용
            # k - 도착, k-1 경유, k-2 출발지
            s += bat[A[j]][A[j+1]]
        s += bat[A[k-1]][A[0]]  # 마지막 경유지 -> 사무실로 이동하는 배터리 소비량
        print(s)

    else:
        for j in range(i, k):
            A[i], A[j] = A[j], A[i]
            f(i+1, k)
            A[i], A[j] = A[j], A[i]



n = int(input())
bat = [list(map(int, input().split())) for _ in range(n)] # 배터리 소비량
A = [a for a in range(n)]
f(0,n)