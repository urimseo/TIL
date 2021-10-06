'''
1. 총 상자를 옮기는 횟수 = move
2. 입력 받은 리스트 = box
3. box 리스트의 maxb 를 구하고
4. box 리스트의 minb 를  구한다.
5. maxb -1, minb +1 을 하면 총 1번의 이동
6. 이동할때마다 move--
7. 문제는 이동한 이후의 리스트를 어떻게 처리할것인가...?
8. 최대값의 인덱스를 찾기
9. 그 최대값의 인덱스에 + - 1 한 값을 재할당.
'''

a_list = [3, 2, 6, 5, 4, 1]

moves = 5

# for x in range(moves):
while moves > 0:
    max_v = 0
    min_v = 101
    max_idx = -1
    min_idx = -1
    for i, v in enumerate(a_list):
        if max_v < v:
            max_v = v
            max_idx = i
    a_list[max_idx] = (max_v - 1)

    for i, v in enumerate(a_list):
        if min_v > v:
            min_v = v
            min_idx = i
    a_list[min_idx] = (min_v + 1)

    moves -= 1
print(a_list)
        # if min_v > v:
        #     min_v = v
        #     min_idx = i
        #     a_list[min_idx] = (min_v + 1)
# print(a_list)

# print(a_list)

    # for i, v in enumerate(a_list):
    #     print(a_list)
#         if min_v > v:
#             min_v = v
#             min_idx = i
#
#         a_list[min_idx] = min_v + 1
#     moves -= 1
# print(a_list)





# move = int(input())
#
# for i in range(move):
