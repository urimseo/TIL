'''
A -> 1~ 12까지의 원소가짐
for a in range (1, 13):
 여기서 부분집합을 전체 만들고,,,
 원소의 수가 n 개인 것을 고른다.

 원소의 합이 k 라면 cnt + 1 해서 출력
,
'''
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a = len(arr) # 원소의 개수
T = int(input())
for tc in range(T):
    ans = 0
    n, k = map(int, input().split())
    for i in range(1 << a):  # 왜 a+1 ?  0 ! 2^n -1  1024 1023 경우의 수 - 2^n개 2^3 -> 8
        # (1<<n-1) (2**n) - 1

        total = 0
        cnt = 0
        for j in range(a):
            if i & (1 << j):
                total += arr[j]
                cnt += 1

        if cnt == n and total == k:
            ans += 1

    print(f'#{tc+1} {ans}')






