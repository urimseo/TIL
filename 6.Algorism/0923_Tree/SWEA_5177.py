'''
이진최소힙
tree = [0] -> 빈 트리 만들고 시작
last +=1
tree[last] = data
# 부모가 있고, 부모 > 자식이면 data 교환

#  자식으로부터 부모 알아내기
c = last -> 자식
p = c//2 -> 부모번호는 자식번호 나누기 2
# 비교하여 변경
while p and tree[p] > tree[c]:
    tree[p] <-> tree[c] 부모 자식 값 변환
    c <- p
    p <- c//2 로 값도 변경해야함

'''

def enq(data):
    global last
    last += 1
    tree[last] = data
    c = last
    p = c//2
    while p > 0 and tree[p]>tree[c]: # 부모가 존재하고, 최소힙 규칙에 어긋나면
        tree[p], tree[c] = tree[c], tree[p] # 값 교환해서 최소힙으로 만들기
        c = p  # 부모를 새로운 자식으로
        p = c//2 # 다시 변경된 자리에서의 부모와 값을 비교하기 위하여 부모를 또 찾아야함.
                 # 부모보다 부모의 부모가 더 크면 또 값을 교환...

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0  # 힙의 마지막 정점 번호
    for x in arr:
        enq(x) # 힙은 우선순위 큐를 사용하기 때문에 enq라고 이름짓기

    # 부모의 부모의..는 반복문으로 돌려서 찾기..
    res = 0
    g = N
    while g > 0:
        g = g//2
        res += tree[g]
    print(f'#{tc} {res}')