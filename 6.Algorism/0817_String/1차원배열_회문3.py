N, M = map(int, input().split())
str1 = input()
ans = -1
for i in range(N-M+1): # 회문인지 확인할 영역의 시작 인덱스
    cnt = 0 # 만일 회문 길이 셀거면 cnt
    for j in range(M//2):  # 비교 횟수, or 비교 위치->(M//2 -1)
        if str1[i+j] != str1[i+M-1-j]: # 모든 경우를 다 비교하게 됨. 일치하게되면 안쪽도 비교하기 때문..?
            break

    else:  # 회문 찾으면 인덱스 적용
        ans = i
        break
if ans != -1:
    for k in range(M):
        print(str1[ans+k], end='')
    print()
else: # 회문이 아닌 경우
    print(ans)


# 다른 회문
# ans = 0
# for i in range(N-M+1):
#     flag = 1
#     for j in range(M//2):
#         if str1[i+j] != str1[i+M-1-j]:
#             flag = 0
#             break
#
#     if flag == 1: # i에서 시작하는 회문
#         ans = i
#         break
# if ans != -1:
#     for k in range(M):
#         print(str[ans + k], end='')
#     print()
# else:
#     print(ans)

