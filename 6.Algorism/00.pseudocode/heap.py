def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = tree[1]         # 루트 백업
    tree[1] = tree[last]  # last를 1에 복사
    last -= 1             # last 하나 감소해서 없는셈 치기.
    p = 1
    c1 = 2*p              # 왼쪽 자식
    c2 = 2*p+1            # 오른쪽 자식
    # 자식이 있는 경우 (하나라도)
    while c1 <= last:
        if c2 <= last:    # 자식이 하나라도 있으면
            if tree[c1] >= tree[c2] and tree[c1] > tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
                p = c1
            elif tree[c1] < tree[c2] and tree[c2] > tree[p]:
                tree[c2], tree[p] = tree[p], tree[c2]
                p = c2
            c1 = p*2
            c2 = p*2+1
        else: # 왼쪽 자식만 있는 경우
            if tree[c1] > tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
                break
        return tmp
    # 1. 왼쪽자식만 있는 경우 - last 가 왼쪽 (자식 하나)



tree = [0]*101    # 최대 100번 노드까지..
last = 0          # 마지막 노드 번호
a = [7, 2, 3, 9, 5]

for x in a:
    enq(x)

deq()