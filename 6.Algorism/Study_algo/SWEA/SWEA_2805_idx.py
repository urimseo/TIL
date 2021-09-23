n = int(input())
lst = input().split()

pos1 = 0
pos2 = (n+1)//2  # 5일때도 3, 6일때도 3... 짝홀 판별 따로 안해도됨 대박
# print(f'#{tc}', end=' ')
for i in range(pos2):
    print(lst[pos1], end=' ')
    if pos2 < n:
        print(lst[pos2], end=' ')
    pos1 += 1
    pos2 += 1
print() # 다음 테케에서 줄바꿈


