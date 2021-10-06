n = int(input())
card = list(map(int, input()))
# card = '49679'

c = [0] * 11

for i in card:
    c[i] += 1
maxV = -1
cnt = -1
for i in range(11):
    if c[i] >= cnt:
        cnt = c[i]
        maxV = i

print(maxV, cnt)