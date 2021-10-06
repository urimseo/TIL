'''
노드의 합
'''
'''
for tc in range(1, int(input())+1):
    N, M, L = map(int,input().split())
    tree = [0]*(N+1) # 비어있는 완전이진트리 생성

    for i in range(M):
        n, m = map(int,input().split())
        tree[n] = m
    p = N

    for i in range(N, -1, -1):
        p = i//2 # 부모노드에
        tree[p] += tree[i] # 자식노드 값 더하기

    print(f'#{tc} {tree[L]}')


'''

# 함수로 재귀호출하여 풀기

def f(n, V):
    if n > V: # 오른쪽 자식이 없을 경우 r2에서 idx 초과함. 마지막 노드의 경우 오른쪽 자식이 없을 수 있다.
        return 0 # 0을 리턴하지 않으면 None타입이 return 되어 r1 + r2가 typeerror로 더해질 수 없다.
    else:
        if tree[n] > 0:  # 리프노드에 도착하면 값이있음
            return tree[n]  # 값이 있으므로 리턴 해서 r1이나 r2 에 들어감 (호출한 함수에 들어감)
        else:
            r1 = f(2*n, V)  # 왼쪽자식
            r2 = f(2*n+1, V)  # 오른쪽 자식 -> 없을 수도 있으니 걸러내는 과정이 필요함
            tree[n] = r1 + r2
            return tree[n]

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)  # 비어있는 완전이진트리 생성

    for i in range(M):
        n, m = map(int, input().split())
        tree[n] = m
    f(1, N) # 여기서의 return 값은 버리면 됨. 우리가 필요한 것은 tree[L] 이기 때문

    print(f'#{tc} {tree[L]}')