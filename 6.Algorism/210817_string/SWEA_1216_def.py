
def palindrome(arr, varr):
    for m in range(100, 0, -1): # 회문의 길이 m 줄어들면서 99 ~ 0 까지
        for i in range(100): # 행 탐색
            for j in range(100-m+1): # 열 탐색
                tmp = arr[i][j:m+j]
                tmp2 = varr[i][j:m+j]
                if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:  # 회문 탐색
                    return m

for i in range(1, 11):
    T = int(input())
    arr = [list(input())for _ in range(100)] # 가로 리스트
    varr = list(zip(*arr[::-1])) # 세로 리스트
    print(f'#{T} {palindrome(arr, varr)}')
