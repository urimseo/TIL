s = input()

stack = []
ans = 1
for x in s:
    if x == '(': #Push
        stack.append(x)
    elif x == ')': # pop한 결과와 비교, 스택이 비어 있으면 오류 (중단)
        if stack: # 스택이 비어있지 않으면
            stack.pop() # 소괄호만 있으므로 비교 생략
        else:
            break # 닫는 괄호가 나왔으나, 여는 괄호 부족
            ans = 0

    else:
        pass  # 괄호 아닌 경우
# 스택에 남은 여는 괄호가 없는지 확인.
if ans and stack:  # 닫는 괄호가 더이상 없으나 여는 괄호가 남은 경우
    ans = 0
print(ans)