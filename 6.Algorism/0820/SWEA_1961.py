'''
숫자 배열 회전
'''
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = [list(map(str, input().split())) for _ in range (n)]
    lst_1 = list(zip(*lst[::-1])) # 90
    lst_2 = list(zip(*lst_1[::-1])) # 180
    lst_3 = list(zip(*lst_2[::-1])) # 270

    new_list = []
    for i in range(n):  # 리스트의 첫번째 줄끼리 합치기
        new_list.append(list(lst_1[i]))
        new_list.append(list(lst_2[i]))
        new_list.append(list(lst_3[i]))

    join_list = []
    for i in new_list:
        join_list.append(''.join(i))

    print(f'#{tc}')
    for i in range(0, n*n, 3):
        final = join_list[i:i+3]
        for j in final:
            print(j, end=' ')
        print()



