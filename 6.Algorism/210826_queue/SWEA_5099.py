'''
피자
n - 화덕의 크기
m - 피자의 개수

'''

# n, m = map(int(input().split()))
# pizza = list(map(int(input().split())))
n, m = 3, 5
pizza = [7, 2, 6, 5, 3]
# 피자의 번호를 따로 저장해야하나..?
pnum = {}
for i in range(m-1, -1, -1 ):
    pnum[i] = pizza[i]
print(pnum)
# {4: 3, 3: 5, 2: 6, 1: 2, 0: 7}
# {0: 7, 1: 2, 2: 6, 3: 5, 4: 3}

b = pnum.popitem()
print(b[0])
print(pnum)
oven = []

#
while pizza:
    if len(oven) < n: # 화덕의 크기보다 작으면 크기만큼 넣기
        first = pizza.pop(0)
        oven.append(first)
    # oven = [7, 2, 6]
    print(oven)
    if len(oven) > 1:
        again = oven.pop(0) // 2  # 치즈가 녹은 정도
        if again <= 0: # 만약 치즈가 다 녹았으면
            oven.pop(again) # 오브에서 빼고
            next = pizza.pop(0) # 다음 피자 나오시고
            oven.append(next) # 입장하세요~
        else:# 안녹았으면
            oven.append(again) # 다시들어가세요~
    elif len(oven) == 1:
        print(oven[0])
