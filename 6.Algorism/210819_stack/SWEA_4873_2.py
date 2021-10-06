
# ㄱㅁㅊ
# T = int(input())
# for t in range(1, T + 1):
#     s = input()
#     stack = [0] * 1000
#     top = -1
#     for c in s:
#         if top < 0 or stack[top] != c:  # i) 스택이 비어있거나, ii) 마지막으로 넣은 요소와 다를 경우
#             top += 1
#             stack[top] = c
#         else:  # 스택에 문자 요소가 있고, 마지막 넣은 요소와 같을 경우
#             top -= 1
#
#     print(f'#{t} {top + 1}')



# ㅇㅁㅎ
T = int(input())
for tc in range(1, T + 1):
    string = input()
    stack = []

    for s in string:
        if not stack:  # 스택이 비어있는 경우, 값 추가
            stack.append(s)
        elif stack[-1] == s:  # 맨 마지막 값이 현재 넣으려는 값과 일치하는 경우
            stack.pop()  # 맨 마지막 값 제거
        else:  # 맨 마지막 값이 현재 넣으려는 값과 다른 경우, 스택에 추가
            stack.append(s)

    print(f'#{tc} {len(stack)}')  # 길이 출력