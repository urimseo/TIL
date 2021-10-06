for tc in range(1, 11):
    n = int(input())
    s1=input()
    #
    # step1 - 후위표기법
    stack=[]
    s2=''
    for x in s1:
        if '0' <= x <= '9':
            s2 += x
        elif x == "*": # *는 우선순위가 + 보다 높으니 그냥 저장
            stack.append(x)
        elif x =="+": # 우선순위 낮아서 앞의 stack에 있는것 전부 빼서 계산식에넣고
            while stack:
                s2 += stack.pop()
            stack.append(x) # 전부 pop해서 stack이 비어있으면 넣기
    while stack:
        s2 += stack.pop() # 스택에 남은 연산자 모두 계산식에 넣기

    # step2 계산
    for x in s2:
        if x=="+":
            op1=stack.pop()
            op2=stack.pop()
            stack.append(op2+op1)
        elif x=="*": # 연산자는 피연산자 2개 pop
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 * op1) # 계산해서 넣음
        else:       # 피연산자는 그냥 스택에 넣고 연산자를 기다림.
            stack.append(int(x))
    print(f'#{tc} {stack.pop()}')

