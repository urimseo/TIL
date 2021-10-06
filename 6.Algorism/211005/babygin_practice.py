'''
존재하는 알파벳이 몇개 있는가?
ABCACDPO

A: 2
B: 1
C: 2
D: 1
P: 1
O: 1

'''

#######dictionary로 알파벳 세기 ###########
# alpha = 'ABCACDPO'
# dic = {}
# for i in alpha:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# for i in dic:
#     print(f'{i}: {dic[i]}')

# A부터 Z까지 출력
#ord('A') ~ ord('Z') # 65 ~ 90 -> 총 26개
# for ch in range(ord('A'), ord('Z')+1):
#     print(chr(ch), end=' ')

####이중포문으로 출력하기####
# for ch in range(ord('A'), ord('Z')+1):
#     # ch가 하나 선택되었으면 alpha 에서 몇개 있는지 세주기
#     cnt = 0
#     for i in range(len(alpha)):
#         if alpha[i] == chr(ch):
#             cnt += 1
#     if cnt == 0 : continue
#     print(f'{chr(ch)} : {cnt}')

####cnt 배열 만들어서 출력 ######
# cnt = [0] * (ord('Z')+1)
# for i in range(len(alpha)):
#     idx = ord(alpha[i])
#     cnt[idx] += 1
#
# for ch in range(ord('A'), ord('Z')+1):
#     if cnt[ch]:
#         print(f'{chr(ch)} : {cnt[ch]}')

# cnt[ord('A')] = cnt[65]


#######리스트 안에 있는 숫자 세기##########
# lst = [3, 2, 1, 9, 10, 5, 5] # 제한조건 : 0<= 숫자 < 20
#
# cnt = [0] * 20
# for i in lst:
#     cnt[i] += 1
# for k in range(len(cnt)):
#     if cnt[k]:
#         print(k, end=' ')
#         # print(f'{k} : {cnt[k]}개')

town = [[3, 10, 5, 7],[6, 15, 9, 8]] # 마을 -> 번호는 1~20
black_list = [9, 8, 3, 1, 20] # 블랙리스트
cnt = 0
###방법1 - 내가한것###

# for t in town:
#     for i in t:
#         if i in black_list:
#             cnt += 1
# print(f'{cnt} 명')


###방법2 - 풀이###
# black 에 있는 리스트 표시하기
# is_black = [0]*21
# for i in black_list:
#     is_black[i] = 1
#
# for y in range(len(town)): # 2
#     for x in range(len(town[y])): # 4
#         val = town[y][x]
#         if is_black[val] == 1:
#             cnt += 1
# print(f'{cnt} 명')
'''
#################아나그램#############
A = 'EVERLAND'
B = 'LAVENDER' 
 아나그램 검사하는 소스코드 만들기 
- STR  두개 입력 
- 두개가 아나그램인지 검사하는 소스코드 
'''

# ana1 = input()
# ana2 = input()
# cnt1 = [0] * (ord('z') + 1)
# cnt2 = [0] * (ord('z') + 1)
# for i in range(len(ana1)):
#     cnt1[ord(ana1[i])] += 1
#     cnt2[ord(ana2[i])] += 1
# if cnt1 == cnt2:
#     print('아나그램입니다.')
# else:
#     print('아나그램이 아닙니다.')

# flag = '아나그램입니다'
# for i in range(200):
#     if cnt1[i] != cnt2[i]:
#         flag = '아나그램이 아닙니다.'
#         break
# print(flag)



