'''
피자
n - 화덕의 크기
m - 피자의 개수

'''
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    pizza = []
    # 피자의 번호를 따로 저장
    for k, v in enumerate(lst):
        pizza.append([k, v])
    oven = []

    for i in range(n):  # 화덕크기만큼 초기세팅
        oven.append(pizza.pop(0))

    while len(oven) > 1:  # 오븐에 피자가 하나 남을때까지
        first = oven.pop(0)  # 첫번째 피자를 꺼내고
        first[1] = first[1] // 2  # 치즈는 반 녹은 상태
        if first[1] > 0:  # 치즈가 다 안녹았으면
            oven.append(first)  # 다시들어가세요~
        elif pizza:  # 다음 피자가 있다면
            oven.append(pizza.pop(0))  # 새로입장

    print(f'#{tc} {oven[0][0] + 1}')


