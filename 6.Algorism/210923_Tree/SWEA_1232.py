'''
사칙연산
중위순회: LVR
후위순회: LRV
전위순회: VLR

'''

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
'''



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

def calc(v):
    if len(tree[v])==2:
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R # //로 처리하지 않는다.



for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        tmp = input().split()
        # 왼쪽 자식 , 오른쪽 자식 , 숫자 모두 str 형태 -> 먼저처리를 하기
        tree[int(tmp[0])] = tmp
        # 0 : 정점 번호, 1: 연산자, 2: 왼쪽 자식, 3: 오른쪽 자식
        if len(tmp) ==4:
            tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
            tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
        else:
            tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])


    print(f'#{tc} {int(calc(1))}')

#################################################################################

def calc(v):
    if len(tree[v])==2:
        return tree[v][1]
    else:
        L = calc(int(tree[v][2]))
        R = calc(int(tree[v][3]))

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R # //로 처리하지 않는다.



for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        tmp = input().split()
        tree[int(tmp[0])] = tmp
        # 0 : 정점 번호, 1: 연산자, 2: 왼쪽 자식, 3: 오른쪽 자식
        if len(tmp) ==4:
            tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
            tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
        else:
            tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])


    print(f'#{tc} {calc(1)}')






