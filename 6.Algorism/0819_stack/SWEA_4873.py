'''
반복문자 지우기
-> 반복문자 있으면 지우고 합치고 반복
'''
# T = int(input())
# for tc in range(1, T+1):
#
#     char = list(input())
#     i = 0
#     while i < len(char)-1:
#         if char[i] == char[i+1]:
#             char.pop(i)
#             char.pop(i)
#             i = 0
#         else:
#             i += 1
#     print(f'#{tc} {len(char)}')

T = int(input())
for tc in range(1,T+1):
    char = input()
    stack = []
    for i in char:
        if not stack or stack[-1] != i: # 스택이 비어있거나 or 스택의 마지막 원소와 같지 않아도 넣음
            stack.append(i)
        elif i == stack[-1]: # stack의 마지막 값과 같으면 pop
            stack.pop()

    print(f'#{tc} {len(stack)}')

