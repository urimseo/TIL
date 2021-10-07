'''
퀵 정렬
-  pivot 값 설정
 - pivot 보다 큰값 오른쪽, 작은값, 왼쪽에 위치
'''

def hoare(lst, l, r):
    i, j = l, r
    x = lst[l]
    while i <= j:
        while i <= j and lst[i] <= x:
            i += 1
        while i <= j and lst[j] >= x:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j


def qsort(lst, l, r):
    if l < r:
        p = hoare(lst, l, r)
        qsort(lst, l, p-1)
        qsort(lst, p+1, r)


for tc in range(1, int(input())+1):
    n = int(input())
    lst = list(map(int, input().split()))
    qsort(lst, 0, n-1)

    print(f'#{tc} {lst[n//2]}')