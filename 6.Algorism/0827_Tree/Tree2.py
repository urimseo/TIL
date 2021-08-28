'''
포화이진트리 or 완전 이진트리
'''

def pre_order(n, last):
    if n <= last: # 곱했더니 마지막 정점 넘어간거면 없는것 . 포화 이진트리에 한정됨
        print(tree[n], end=' ')
        pre_order(n*2, last)  # 왼쪽
        pre_order(n*2+1, last) # 오른쪽



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


last = 8
tree = []