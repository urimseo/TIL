'''
부분집합의 합 문제 구현하기
a = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
'''

a = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(a)
cnt = 0
for i in range(1, 1 << n):  # 1~2^n-1 까지
    subset = []
    s = 0
    for j in range(n): # n 번돌기.
        if i & (1 << j):
            s += a[j]
            subset.append(a[j])
    if s == 0:
        cnt += 1
        print(subset)
print(cnt)