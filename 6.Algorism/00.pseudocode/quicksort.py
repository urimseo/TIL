'''
퀵정렬
10: 3~4
'''
import sys
sys.stidin = open("백만개.txt", "r")

def lomuto(A, p, r):
    i = p - 1
    x = A[r]
    for j in range(p, r):
        if A[j] > x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def hoare(A, l, r):
    i, j = l, r
    x = A[l]
    while i <= j:
        while i <= j and A[i] <= x:
            i += 1
        while i <= j and A[j] >= x:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def qsort(A, l, r):
    if l < r:
        p = hoare(A, l, r)
        # p = lomuto(A, l, r)
        qsort(A, l, p-1)
        qsort(A, p+1, r)

# A = [7, 3, 5, 1, 2, 8, 4]
A = list(map(int, input().split()))
qsort(A, 0, 999999)
# qsort(A, 0, 6)
print(A[50000])