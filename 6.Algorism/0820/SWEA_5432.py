'''
쇠막대기 자르기
스택에 들어있으면 쇠막대기
레이저 만나면 pop
() ((( () () ) ( () ) () ))( () )
-(면 stack에 넣고,
-)만나고, 이전거가 (이면 pop
- 그렇지 않으면,,, stack에서 -1
'''

T = int(input())
for tc in range(1, T+1):
    bk = input()
    stack = [] # push
    res = 0 # 막대기 개수
    for i in range(len(bk)):
        if bk[i] == '(':
            stack.append(bk[i])
        elif bk[i] == ')' and bk[i-1] == '(':  # 레이저면 현재 stack 개수 더하기
            stack.pop()
            res += len(stack)
        else:  # 레이저가 안나왔는데 막대기가 끝났으면
            res += 1  # 하나의 막대기는 생기니까 더해주고
            stack.pop()  # stack 에서 제거
    print(f'#{tc} {res}')
