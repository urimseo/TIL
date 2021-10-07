'''
이진탐색
'''

def binary_search(A, k, s, e, flag):
    global res
    if s > e:  # 시작점이 끝점보다 작을때만 실행 하도록
        return
    else:
        m = (s+e)//2
        if k == A[m]:  # key 값이 중간값과 같을때
            res += 1  # key 찾으면 res ++
            return
        elif k < A[m]:  # 찾을 값이 m 보다 작으면, 왼쪽
            if flag == 1:
                return
            binary_search(A, k, s, m-1, 1)  # 왼쪽의 경우 flag = 1이됨. 만약 flag 가 1 인 상태에서 들어오면 return
        else:
            if flag == 2:  # flag가 2인 상태에서 들어오면 이전의 탐색이 오른쪽에서 진행되었다는 것이므로 조건에 위배되어 그냥 return 하고 종료
                return
            binary_search(A, k, m+1, e, 2)  # 오른쪽의 경우 flag = 2.

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    res = 0  # 조건에 맞는 찾은 탐색 횟수 ++
    for b in B:
        binary_search(A, b, 0, N-1, 0)  # 찾을값, 시작 인덱스, 마지막 인덱스, flag 로 왼쪽 오른쪽 표시

    print(f'#{tc} {res}')
