N = int(input())
pole = [0]*1001
maxH = [0]*1002
for _ in range(N):
    idx, h = map(int, input().split())
    pole[idx] = h

maxH[1000] = pole[1000]
for i in range(999, 0, -1):
    maxH[i] = max(maxH[i+1], pole[i])
print(maxH[:20])
area = pole[0]  # 첫 기둥 높이는
print(area)
for i in range(1, 1001):
    if pole[i-1]>pole[i]:
        if pole[i-1]<=maxH[i+1]:  # 다음 기둥이 더 크면 앞에가 작으니 앞에껄로
            pole[i] = pole[i-1]
        else:
            pole[i] = max(pole[i], maxH[i+1])  # 앞의 기둥이 더 크면 뒤에랑 비교해서 큰걸로..?
    area += pole[i]
print(area)