'''
Forth
'''

t = int(input())
for tc in range(1, t+1):
    n = input().split()
    stack = []
    error = 0
    while error == 0:
        for i in n:
            if i.isdigit():
                stack.append(int(i))
            else:
                if i == ".":
                    if len(stack) == 1:
                        error = stack.pop()
                    else:
                        error = 'error'
                        break
                elif i == "+" and len(stack) >= 2:
                    op1=stack.pop()
                    op2=stack.pop()
                    stack.append(op2+op1)
                elif i == "-" and len(stack) >= 2:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 - op1)
                elif i == "*" and len(stack) >= 2:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 * op1)
                elif i == "/" and len(stack) >= 2:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 // op1)  # 그냥 나눗셈 /하면 float 형식이 된다.
                else:
                    error = 'error'  #
                    break

    print(f'#{tc} {error}')

