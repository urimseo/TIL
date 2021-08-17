
#
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n - 행, m - 회문 길이
    arr = [(input()) for _ in range(n)]
    # res = ''

    # 세로 검색 리스트 생성
    vtmp = []
    for j in range(n):
        tmp = ''
        for i in range(n):
            tmp += (arr[i][j])
        vtmp.append(tmp)

    # 가로 길이 회문 탐색
    for i in range(n):
        tmp = ''  # 가로탐색
        tmp2 = ''  # 세로탐색
        for j in range(n-m+1):
            tmp = arr[i][j:m+j]  # 가로탐색  m 만큼 슬라이싱
            tmp2 = vtmp[i][j:m+j]  # 세로탐색 m 만큼 슬라이싱
            if tmp == tmp[::-1]:  # 회문 탐색
                res = tmp
                break
            elif tmp2 == tmp2[::-1]:
                res = tmp2
                break
    print(f'#{tc} {res}')



'''

'''




