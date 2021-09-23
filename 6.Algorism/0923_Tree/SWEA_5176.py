'''
TREE의 특징
V개의 정점
E개의 간선 (E+1 = V)

3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''

def f(n):
    global cnt
    if n:
        cnt += 1 # 전위순회  -> 중위, 후위도 상관없음
        f(ch1[n])
        f(ch2[n])
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1 # 1번부터 V번까지 정점 번호
    ch1 = [0] * (V+1)  # 자식1 혹은 왼쪽 자식, 부모를 인덱스로 자식번호 저장
    ch2 = [0] * (V+1)  # 자식2 혹은 오른쪽자식
    arr = list(map(int, input().split()))
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1]  # 부모 n1, 자식 n2
        if ch1[n1] == 0: # 자식1이 아직 없으면
            ch1[n1] = n2  # 1에 저장
        else: # 자식1이 있으면
            ch2[n1] = n2  # 2 에 저장
    cnt = 0 # 방문한 정점수
    f(N) # N부터 순회

    print(f'#{tc} {cnt}')
