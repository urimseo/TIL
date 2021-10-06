
n, m = map(int, input().split())
# n개의 정수, m개의 구간합
lst = list(map(int, input().split()))
total = []
for i in range(n-m+1):
    res = 0
    for j in lst[i:i+m]:
        res += j
    total.append(res)
print(max(total) - min(total))
