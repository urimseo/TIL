'''
주사위쌓기
'''
n = 6 # 주사위 면
m = int(input())  # 쌓는 수
dice= [list(map(int, input().split())) for _ in range(m)]
maxV = 0
for k in range(1, 7): # 주사위 번호 1~6
    onelist = []
    for one in dice:
        for i in range(n):
            if one[i] == k:  # 밑면은 1-6까지 모든 경우 검사
                tmp = one[::]  # 깊은 복사로 임시 리스트 생성
                if i == 0: # 마주보는 면 모두 pop 하고 나머지에서 최댓값 구하기
                    tmp.pop(0) # 밑
                    k = tmp.pop() # 윗면 -> 다음 윗면이 됨
                elif i == 1:
                    k = tmp.pop(3) # 윗
                    tmp.pop(1) # 밑
                elif i == 2:
                    k = tmp.pop(4) # 다음 윗
                    tmp.pop(2)
                elif i == 3:
                    tmp.pop(3)
                    k = tmp.pop(1)
                elif i == 4:
                    tmp.pop(4)
                    k = tmp.pop(2)
                elif i == 5:
                    tmp.pop()
                    k = tmp.pop(0)
                onelist.append(max(tmp)) # 다더해
                break
    if maxV < sum(onelist):
        maxV = sum(onelist)
print(maxV)


