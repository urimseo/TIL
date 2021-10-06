'''
어디에 단어가 들어갈 수 있을까
'''

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst2 = [[0]*(n+1) for _ in range(n+1)]
    # 끝에 벽 붙이고 밑에 0 붙이기
    for i in lst:
        i.append(0)
    zero = [0]*(n+1)
    lst.append(zero)
    # 세로 리스트 만들기
    for i in range(n+1):
        for j in range(n+1):
            lst2[j][i] = lst[i][j]

    res = 0
    for i in lst:  # 하나의 리스트씩 보는데
        cnt = 0
        for j in range(n+1):  # 인덱스 접근할 j
            if i[j] == 1:  #현재 1이면 cnt ++
                cnt += 1
                if i[j+1] == 1:  # 다음도 1이면 계속
                    continue
                elif cnt == m and i[j+1] != 1: # 현재 cnt와 문자열 길이가 같고, 다음번이 벽(0)이면
                    res += 1  # 찾았음 추가
                    cnt = 0
                else:
                    cnt = 0
    for i in lst2: # 세로
        cnt = 0
        for j in range(n+1):
            if i[j] == 1:
                cnt += 1
                if i[j+1] ==1:
                    continue
                elif cnt == m and i[j+1] != 1:
                    res += 1
                    cnt = 0
                else:
                    cnt = 0
    print(f'#{tc} {res}')

'''ㅇㅊㅎ
TC = int(input())
  
for tc in range(TC):
    N, K = map(int, input().split())
    # a = '1011101111101110' 처럼 문자열로 더할 수 있도록 str형식으로 가져오기
    #N:배열의 크기
    #K:단어의 길이
    arr = [input().split() for _ in range(int(N))]
    # print(arr)  #[['0', '0', '1', '1', '1'], ['1', '1', '1', '1', '0'], ['0', '0', '1', '0', '0'], ['0', '1', '1', '1', '1'], ['1', '1', '1', '0', '1']]
  
    #1. 행의 합 & 열의 합
    chunk_list_r = []
    chunk_list_c = []
    chunk_list = []
    for i in range(N):
        tmp_chunk_r = ''
        tmp_chunk_c = ''
        for j in range(N):
            tmp_chunk_r += arr[i][j]
            tmp_chunk_c += arr[j][i]
        # print(tmp_chunk_r) 00111 11110 00100 01111 11101
        # print(tmp_chunk_c) 01001 01011 11111 11010 10011
        chunk_list.append(tmp_chunk_r)
        chunk_list.append(tmp_chunk_c)
  
    #2. '0'을 기준으로 split 해서 리스트에 1이 들어간 스트링만 남기기
  
    new_list = []
    for chunk in chunk_list:
        new_list.extend(chunk.split('0'))     #chunk.split('0')의 출력물이 리스트니까, extend로 인자들만 result_list에 넣어주기
    # print(new_list)
    #['', '', '111', '', '1', '', '1', '1111', '', '', '1', '11', '', '', '1', '', '', '11111', '', '1111', '11', '1', '', '111', '1', '1', '', '11']
  
    count = 0
    for i in new_list:
        if len(i) == K:
            count += 1
  
    print(f'#{tc+1} {count}')
'''
