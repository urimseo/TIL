'''
mst
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
#
def prim1(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    MST[r] = 1
    key = [10000]*(V+1) # 가중치의 최대값 이상으로 초기화/ key[v]는 v 가 MST 에 속한 정점과 연결될 떄의 가중치
    key[r] = 0          # 시작 정점의 key
    for _ in range(V):  # V+1 개의 정점 중 V 개를 선택
        # MST에 포함되지 않은 정점 중(MST[u] == 0), key 가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i]<minV:
                u = i
                minV = key[i]
        MST[u] = 1      # 정점 u를 MST 에 추가
        # u에 인접인 v 에 대해 MST 에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v]>0:        # 인접이면서 포함되지 않은걸 찾으면 key[v] 갱신
                key[v] = min(key[v], adjM[u][v])    # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    # 각 정점이 MST 를 구성했을떄의 weight 의 총 합의 최솟값을 구해야 한다.
    return sum(key)

def prim2(r, v):
    MST = [0]* (V+1)    # MST 포함 여부
    MST[r] = 1
    s = 0  # 누적 비용 계산
    for _ in range(V):
        u = 0
        minV = 10000
        # MST 에 포함된 정점i와 인접한 정점 중 MST 에 포함되지 않고 가중치가 최소인 정점 u 찾기
        for i in range(V+1):
            if MST[i] == 1:           # MST 포함된 것 찾기
                for j in range(V+1):  # 인접한 것 찾기
                    if adjM[i][j] >0  and MST[j] == 0 and minV > adjM[i][j]: # 인접하고, 포함되어있지 않아야하고 그 중 가중치가 가장 작은애라면
                        u = j
                        minV = adjM[i][j]
                        # 이렇게하면 u 가 찾아짐. 그리고 이걸 추가로 MST 에 넣는다
        # MST 에 포함된 모든 애들 중 인접한 애들 사이에서 최소인 애ㅑ들 찾아서 가산하기
        s += minV  # 비용 계속 계산
        print(minV)
        MST[u] = 1

        # MST에 minV 를 더하고 sum해도 되지 않을까
        # 비용 으로 포함여부 표시하기
        # 안됨!!!-> minV의 초기값은 10000임... 없는 정점번호가 1000으로 표시된다

        # 이걸 반복함으로써 MST 에 포함된 정점은 점점 늘고 그 나머지 인접한 애들 중에 또 비용이 최소인 애들 계속 찾기..
        # 이걸 반복하면서 내가 찾고자 하는 것은 내가 방금전에 선택한 최소비용(minV) 이 MST 를 구성하는 비용 (i,v)가누적하는 비용... 이러면 최소 비용이 구해진다..?
    print(MST)
    return s



V, E = map(int, input().split())

# 인접 행렬 저장
adjM = [[0]*(V+1) for _ in range(V+1)]
# 인접 리스트 저장
adjL = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프
    # 인접 리스트
    adjL[u].append((v, w))
    adjL[v].append((u, w))

print(adjM)
print(adjL)

print(prim1(0, V))  # 175
print(prim2(0, V))  # 175
