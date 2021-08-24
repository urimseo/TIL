for tc in range(10):
    length = int(input())
    before = input()

    # step1
    stack_operator = []  # 연산자
    after = ''  # 피연산자 & /우선순위 높은 연산자는 스택에서 빼서 그때그때 쌓아감.
    for x in before:
        if '0' <= x <= '9':  # 피연산자는 바로 출력(after에 더함)
            after += x
        else:  # 연산자는 #연산자별로 우선순위 일일이 적용해주기.

            if x == '(':  # 들어오는 것: icp : 3 // isp에서 이것보다 낮은것은? 모두! //
                stack_operator.append(x)

            elif x == ')':
                while stack_operator and stack_operator[ -1] != '(':
                    after += stack_operator.pop()
                stack_operator.pop()

            elif x == '+':  # 들어오는 것: icp : 1 // isp에서 이것보다 낮은것은? '(' // 이거나 빈스택일 때 '+'가 들어감
                if not stack_operator:  # 스택이 비어있으면 바로 넣어줌.
                    stack_operator.append(x)

                else:  # 스택에 뭔가 있으면,
                    # while stack_operator[-1] != '(' or stack_operator:    #첫 1번은 무조건 돎 (앞이든 뒤든 충족은 할 것이므로/앞 if문에서 한번 걸렀으므로! / 둘 중 하나가 맞으면 or니까 둘 중하나는 무조건 맞겠지..stack_op가 있으니)
                    # pop되버리면 인덱스에러가 날 수도 있는 것이 --> pop하면 스택에 원래 인자가 1개밖에 없었으면 비게 되는것이므로! / 없는데 마지막 요소[-1]를 가지고 오라고 하니까!인덱스 에러가 날 수밖에 없음.
                    while stack_operator and stack_operator[
                        -1] != '(':  # 스택의 값이 '있으면서'(선제조건) 그 마지막 값이 '('이 아닐 때 돌아감 / #스택이 비거'나' 스택의 마지막 값이 '(' 이면 while 종료
                        # 종료조건: 둘다 만족할 때를 제외한 모든 조건에서 종료!
                        # 다른 연산자들은 다 빼줌. / pop해서 after에 붙여줌.(우선순위연산자들/after계산식에들어가 나중에 먼저 꺼내질애들)
                        after += stack_operator.pop()  # 빼주다가, 스택의 마지막 값이 '('을 만나거나 스택에 값이 없어지면 그때 while 종료
                    # '('을 만났을 때나 스택의 값이 없을 때 그때 스택에 '+'넣어줌
                    stack_operator.append(x)


            elif x == '*':  # 들어오는 것: icp : 2 // isp에서 이것보다 낮은것은? '+', '-', '('
                if not stack_operator:  # 스택이 비어있으면 바로 넣어줌.
                    stack_operator.append(x)

                else:  # 스택에 뭔가 있으면,
                    # while stack_operator[-1] != '(' or stack_operator:
                    while stack_operator and stack_operator[-1] not in ['+', '-',
                                                                        '(']:  # 스택의 값이 있는데 그 마지막 값이 '+', '-'나 '('이 아닐 때 돌아감 / 스택이 비거나 스택의 마지막 값이 '+', or '-' or '(' 이면 while종료
                        # 스택의 마지막 값이 '+', '-'나 '('일 때, while종료, 스택에 값이 없으면 while 종료
                        # 다른 연산자들은 다 빼줌.
                        after += stack_operator.pop()  # 빼주다가, 스택의 마지막 값이 '-'나 '('을 만나거나 스택에 값이 없어지면 그때 while 종료
                    # '-'나 '('을 만났을 때나 스택의 값이 없을 때 그때 스택에 '*'넣어줌
                    stack_operator.append(x)

    while stack_operator:  # 연산자도 마저 스트링 뒤에 붙여줌 #스택이 0이 될 때까지
        after += stack_operator.pop()  # 이 자체가 스택의 마지막 값인가봄!
    # print(after)    #952*+1+33*7*6*9*1*7*+1+86*+61*1*5*2*4*7*+43*8*2*6*+78*4*5*+3+7+2+6+5+1+7+6+73*6*+2+6+62*+4+22*+49*3*+

    # step2
    stack_calc = []  # 스택
    for x in after:  # 만들어 놓은 after 식을 앞에서부터 계산

        if x == '+':
            # oprd_oprt에서 꺼낸 것이 연산자면
            num1 = stack_operator.pop()
            num2 = stack_operator.pop()
            stack_operator.append(num2 + num1)

        elif x == '*':
            num1 = stack_operator.pop()
            num2 = stack_operator.pop()
            stack_operator.append(num2 * num1)

        else:  # 피연산자
            stack_operator.append(int(x))  # 연산에 쓸 거니까 숫자로 바꿔서 넣기

    # print(stack_operator.pop())
    print(f'#{tc + 1} {stack_operator.pop()}')

"""
stack_operator[-1] != '(' and stack_operator  ==>인덱스에러 남  // '마지막 값이' (이 아니면.. / 여기서 '마지막 값'이라는게 존재하기 위해선 우선 '스택에 값이 있어야'#틀린 이유: while stack_operator[-1] != '(' or stack_operator   ==>인덱스에러 남 // 스택의 '마지막 값'이 '('이 아니거나 스택의 값이 있을 때 / '마지막 값'이라는게 존재하기 위해선 일단 스택에 뭔가 있어야.
                                                                ==>while앞 부분만 본다고하더라도 일단 인덱스접근 자체를 하려면 
#틀린 이유: while