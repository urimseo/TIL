'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
6
1 2 1 3 2 4 3 5 3 6

'''


def pre_order(n):
    if n:
        print(n, end=' ')
        pre_order(left[n])
        pre_order(right[n])


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

pre_order(1)
print()
in_order(1)
print()
post_order(1)

node = ['', 'A', 'C', ]
