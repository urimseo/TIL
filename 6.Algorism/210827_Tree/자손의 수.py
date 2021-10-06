'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
6
1 2 1 3 2 4 3 5 3 6

1 2 4 7 12 3 5 8 9 6 10 11 13
12 7 4 2 1 8 5 9 3 10 6 13 11
12 7 4 2 8 9 5 10 13 11 6 3 1
'''


def pre_order(n):
    global cnt
    if n:
        cnt += 1
        # print(n, end=' ')
        pre_order(left[n])
        pre_order(right[n])


def node(n):  # 후위 순회의 응용 코드
    # 내가 n번 정점에 방문했다.
    if n:  # 나오면서 세는 방법.
        r1 = node(left[n])  # 왼쪽 갔다가
        r2 = node(right[n])  # 오르쪽 갔다가 나오면서 세기.
        return r1 + r2 + 1
    else:  # 존재하지 않은 정점에서는
        return 0


def in_order(n):
    if n:
        in_order(left[n])
        print(n, end=' ')
        in_order(right[n])


def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n, end=' ')


v = int(input())
edge = list(map(int, input().split()))
E = v - 1
left = [0] * (v + 1)
right = [0] * (v + 1)

for i in range(E):
    p, c = edge[2 * i], edge[2 * i + 1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
cnt = 0
pre_order(3)
print(cnt - 1)  # 1의 자손 수 찾기
print(node(3))  #
