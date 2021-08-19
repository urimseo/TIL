
'''
원소만 출력하는법
a = [[1],
     [1, 1],
     [1, 2, 1]]

for i in a:
    for j in i:
        print(j, end=' ')
    print()


pij 1, j =0, or j == i

'''
# 이게 왜 dp문제인지 잘 모르겠다...
#
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[1] * i for i in range(1, n+1)]

    for i in range(2,n):
        for j in range(1,i):
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]

    print(f'#{tc}')

    for i in arr:
        print(*i)  # 언팩하는법
        # for j in i:
        #     print(j, end=' ')
        # print()
