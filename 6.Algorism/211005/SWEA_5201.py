'''
컨테이너 운반
 -N개 컨테이너 M대의 트럭
 - 컨테이너 무게
 - 트럭 적재용량

'''
def f(tru, con):
    global weight
    res = 0
    minV = 50
    for k in range(len(con)):
        if tru == con[k]:
            return cargo.pop(k)
        elif tru - con[k] >= 0 and minV > tru - con[k]:
            minV = tru - con[k]
            idx = k
            res = -1
        elif res != -1:
            res = 1
    if res == -1: return cargo.pop(idx)
    else: return 0
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    weight = 0
    for t in range(m):   # truck
        weight += f(truck[t], cargo)  # 트럭무게, cargo 넘겨주기
    print(f'#{tc} {weight}')

