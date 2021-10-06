'''
병합정렬

N = 5 개라면
[0][1][2][3][4] 이렇게 있고

mid = (s + e-1)//2

분할
s~mid / mid+1 ~ e

if mid > e:
    cnt ++


s -> e-1 사이에 mid 값이있다.
홀수개 -> 오른쪽이 더 많다

'''
def merge(ls, le, rs, re):
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt++
    global cnt
    if lst[le] > lst[re]:
        cnt += 1
    res = [0] * (re-ls+1) # 배열의 길이 만큼 만들기
    a = ls  # 왼쪽 시작점
    b = rs  # 오른쪽 시작점
    t = 0   # res 인덱스로 사용
    while a <= le and b <= re:   # 왼쪽과 오른쪽에서 각각의 시작인덱스가 마지막 인덱스보다 작거나 같으면 -> 배열 안에 res에 넣을 것이 남아있는 것.
        if lst[a] <= lst[b]:     # 왼쪽 배열의 맨 앞값이 왼쪽보다 작으면
            res[t] = lst[a]      # 왼쪽의 값을 res에 복사
            a += 1               # 왼쪽 배열 인덱스 ++
            t += 1               # res 배열 인덱스 ++
        elif lst[b] < lst[a]:    # 반대라면, 오른쪽 값 복사, 오른쪽 인덱스 ++, res 인덱스 ++
            res[t] = lst[b]
            b += 1
            t += 1
    # 한 쪽이 먼저 끝나면 남은 것들을 res 에 넣어야 함
    while a <= le:              # 왼쪽 배열이 남았을 경우
        res[t] = lst[a]
        a += 1
        t += 1
    while b <= re:              # 오른쪽 배열이 남았을 경우
        res[t] = lst[b]
        b += 1
        t += 1

    # res 배열 완성 -> lst 에 복사해주기
    t = 0
    for i in range(ls, re+1):
        lst[i] = res[t]
        t += 1
    return

def merge_sort(s, e):
    if s == e: return  # 하나가 되면 정렬이 완료된 것 (정렬 완료)
    # 분할 [s ~ mid] [mid+1 ~ e]
    mid = (s+e-1)//2
    merge_sort(s, mid)       # 왼쪽 부분 정렬 완료
    merge_sort(mid+1, e)     # 오른쪽 부분 정렬 완료
    merge(s, mid, mid+1, e)  # 하나씩 전부 쪼개진 값을 합치기
    return

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    merge_sort(0, len(lst)-1)  # 시작인덱스 -> 0, 마지막 인덱스 -> len(lst)-1 == n-1
    print(f'#{tc} {lst[N//2]} {cnt}')




'''
def merge(ls,le,rs,re):
    global cnt
    if lst[le] > lst[re] : cnt += 1
    # res 배열에다가 작업후 -> lst 에 복사해주기
    res = [0] * (re-ls+1)
    a = ls
    b = rs
    t = 0
    while a <= le and b <= re :
        if lst[a] <= lst[b] :
            res[t] = lst[a]
            a += 1
            t += 1
        elif lst[b] < lst[a]:
            res[t] = lst[b]
            b += 1
            t += 1
    while a <= le :
        res[t] = lst[a]
        a += 1
        t += 1
    while b <= re :
        res[t] = lst[b]
        b += 1
        t += 1
    # res 배열 완성 -> lst 에 복사해주기 [ls ~ re]
    t = 0
    for i in range(ls, re+1):
        lst[i] = res[t]
        t += 1
    return
def merge_sort(s,e):
    if s == e : return # 정렬 완료
    # 분할 [s ~ mid] / [mid ~ e]            ( mid = (s+e-1)//2 )
    mid = (s+e-1)//2
    merge_sort(s,mid) # [s~mid] 정렬 완료!
    merge_sort(mid+1,e) # [mid+1,e] 정렬 완료!
    merge(s,mid,mid+1,e)
    return
T = int(input())
for tc in range(1, T + 1) :
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    merge_sort(0,len(lst)-1)
    print("#{} {} {}".format(tc, lst[N//2], cnt))
'''


# def merge_sort(A, left, right):
#     m = 0
#     if left < right:
#         m = (left + right) // 2
#         merge_sort(A, left, m)
#         merge_sort(A, m+1, right)
#         merge(A, left, right, m)
#
#
#
#
# def merge(M, l, r, m):
#     pass
#
#
# n = int(input())
# lst = [0] + list(map(int, input().split()))
#
#
#
# merge_sort(lst, 0, n)   # 왼쪽 나누기

