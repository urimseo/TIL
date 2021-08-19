'''
괄호검사
push
if ( or {

pop
if )
elif }

짝이 안맞는 경우
pop 했는데 stack 이 없을 경우
pop 끝냈는데 stack 이 남을 경우
'''

T = int(input())
for tc in range(1, T+1):
    text = input()
    # brackets = ['(', ')', '{', '}']
    res = 1
    a = []
    # bracket = ''
    # for i in text:
    #     if i in brackets:
    #        bracket += i

    for i in text:
        if i == '(' or i == '{':
            a.append(i)

        elif i == ')':
            if a and a.pop() == '(':
                res = 1
            else:
                res = 0 # 맞는걸 찾았을 때, 그 다음에 res가 1로 남아있어서 틀렸을때 0으로 바꿔줘야한다.
                break
        elif i == '}':
            if a and a.pop() == '{':
                res = 1
            else:
                res = 0
                break
        else:
            pass

    if a:  # 남아있으면
        res = 0
    print(f'#{tc} {res}')