
# 거품정렬...
'''
for i : N-1 -> 1  #구간 끝
    for j : 0 -> i-1 # 비교할 왼쪽 원소
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
A원소 출력..!
'''
'''
# 다양한 출력 방법이 존재! 모양이 맞춰지기만 하면 됨. 
print(f'#{tc}', end=' ')
for x in A:
    print(x, end=' ')
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    # i = 미정렬 리스트의 인덱스
    # N = 원소의 수
    # 구간의 끝 => i ->  N-1  , i+1 -> N -2  ...
    # 최대값이 맨 마지막에 정렬되기 때문에 구간은 하나씩 줄어야함
    # N-1, N-2 ... 처럼 점점 구간이 점점 줄어듬
    for i in range(N-1, 0, -1):  # 구간 줄이는 반복문
        for j in range(0, i):  # 줄어든 구간에서 반복
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    print(f'#{tc}', end=' ')
    for x in A:
        print(x, end=' ')
    print() # 반복문 끝날때마다 줄바꾸는 방법!!
