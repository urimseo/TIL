'''
1개의 문자열을 받아서 회문인지 판단하기



str1 = input()
if str1 == str1[::-1]:
    print('회문')
else:
    print('회문아님')

# N = 4
# str1 = input()
# cnt = 0
# for i in range(N//2):
#     1. 같은경우 비교
#     if str1[i] == str[N-1-i]:  # -i 는 뒤에서부터 안쪽으로 들어오는 인덱스임.
#         cnt += 1  # 같은 개수
# if cnt == N//2:  # 비교횟수와 일치한 개수가 같으면
#     print('회문')
# else:
#     print('회문아님 ')

# 2. 다른 경우 break 같으면 cnt++
#     if str1[i] != str[N - 1 - i]:
#         break
#
#     cnt += 1
# if cnt == N//2:
#     print('회문')
# else:
#     print('회문아님 ')


# 인덱스 자체를 활용하려면 while문 활용
str1 = input()
N = 4
i = 0
while i < N//2:
    if str1[i] != str1[N-1-i]:
        break
    i += 1

if i == N//2:
    print('회문')
else:
    print('회문아님 ')

'''



























