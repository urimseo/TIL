for tc in range(1, 11):
    n = int(input())
    s1=input()
    #
    # step1 - 후위표기법
    stack=[]
    s2=''
    for x in s1:
        if x.isdigit(): # 숫자면 넣기
            s2 += x
        else:  # 연산자
            if x == "(": # (는 icp =3, isp - 0  우선순위가 가장  높으니 그냥 저장
                stack.append(x)
            elif x == ')':  # icp - 3, isp - 0
                while stack and stack[-1] != '(': # 여는괄호 나오기진전까지 뺴서
                    s2 += stack.pop()  # s2에 넣고
                stack.pop() # 여는괄호 빼기

            elif x == "+": # icp - 1, isp - 1  우선순위 높은건 *
                if not stack:
                    stack.append(x)
                else:
                    while stack and stack[-1] != '(':
                        s2 += stack.pop()
                stack.append(x)

            elif x == '*': # icp - 2, isp - 2
                if not stack:
                    stack.append(x)
                else:
                    while stack and stack[-1] not in ['+', '(']:  # (나 + 가 있으면 다 뺴야함
                        s2 += stack.pop()
                    stack.append(x)

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

