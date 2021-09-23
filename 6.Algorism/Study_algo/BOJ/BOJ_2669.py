'''
직사각형 네개의 합집합의 면적 구하기
입력은 총 4줄
'''

lst = [list(map(int, input().split())) for _ in range(4)]
total = []

for l in lst:
    for i in range(l[0], l[2]):  # 범위 면적 가로
        for j in range(l[1],l[3]):  # 범위면적 세로
            if [i,j] not in total:
                total.append([i,j])

print(len(total))
