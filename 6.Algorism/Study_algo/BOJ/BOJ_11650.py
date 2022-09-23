'''
좌표 정렬하기
'''

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
lst = sorted(lst, key=lambda x:(x[0], x[1]))

for i in lst:
    print(f'{i[0]} {i[1]}')

# x[0]을 첫기준으로 하고 x[1]까지 꼭 써줘야 다음 정렬 기준이 x[1]이 됨..!!