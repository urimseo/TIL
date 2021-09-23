'''
사칙연산
'''


def f(node):
    if tree[node] not in ['+', '-', '*', '/']:
        return tree[node]
    else:
        r1 = f(ch1[node])
        r2 = f(ch2[node])
        if tree[node] == '+':
            tree[node] = r1 + r2
        elif tree[node] == '-':
            tree[node] = r1 - r2
        elif tree[node] == '*':
            tree[node] = r1 * r2
        elif tree[node] == '/':
            tree[node] = r1 // r2
        return tree[node]


for tc in range(1, 11):
    N = int(input()) # 노드의 수
    tree = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    for i in range(N):
        arr = list(input().split())
        if len(arr) == 2:
            tree[int(arr[0])] = int(arr[1]) # 정수로 저장
        else:
            tree[int(arr[0])] = arr[1] # 연산자는 str
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
    f(1)
    print(f'#{tc} {int(tree[1])}')
     # ch1이랑 ch2로 따로 저장해서 처리




# res = []
# inorder(1, N)
# # ['41', '8', '+', '5', '2', '+', '/', '25', '5', '/', '*']
# stack = []
# for i in res:
#     if i.isdigit():
#         stack.append(i)
#     else:
#         r1 = int(stack.pop())
#         r2 = int(stack.pop())
#         if i == '+':
#             stack.append(r2 + r1)
#         elif i == '-':
#             stack.append(r2 - r1)
#         elif i == '*':
#             stack.append(r2 * r1)
#         else:
#             stack.append(r2 // r1)
#
# print(*stack)

