# ----func----순열만들기
def f(i, N):  # 이 P = [2, 5, 1, 4, 3]순열안의 각 원소값을 P[i] = 2, 5, 1, 4, 3 // 을 열번호로 쓰기. 행번호는 주어진 arr그대로
    if i == N:  # 순열 완성(0부터 N-1까지 다 고려한건가.?)
        # 이 안에 P가 만들어져 있는 것 / [0, 1, 2] / [0, 2, 1] / [1, 0, 2]
        tmp_sum = 0
        for i in range(N):  # 0, 1, 2 (각 행) / 순열이 나오는 족족...
            tmp_sum += arr[i][P[i]]  # arr의 0행을 볼 때, 순열의0열과 매칭
        # 각 순열이 나올 때마다 tmp_sum한 것을 리스트에 어펜드하고 싶은데..!
        sum_list.append(tmp_sum)
        # print(P)    #여기서 계속 뽑아지는 것 같은데..!
        return  # 이건그냥함수가 끝남. 함수가 끝남..결국 밑에 함수를 호출했던 f()자리에 반환되는 값은 없음.
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i + 1, N)
            P[i], P[j] = P[j], P[i]


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # N개의 원소를 가진 순열(중복은 없이, 자리바꾸기 모두 가능한)
    # N개의 원소를 가진 0-> N-1 자릿수를 가진 배열
    # P배열.?
    # 순열만들기를 위한 P먼저 생성
    P = []
    for n in range(N):
        P.append(n)
    # print(P)
    # [0, 1, 2]    #이 세 원소로 나올 수 있는 순열생성
    # [0, 1, 2]
    # [0, 2, 1]
    # [1, 0, 2]
    # [1, 2, 0]
    # [2, 1, 0]
    # [2, 0, 1]
    sum_list = []
    f(0, len(P))  # fn이 이 sum_list = [] 아래로 내려와야함!
    # print(sum_list) #[12, 9, 8, 13, 17, 9]

    minidx = 0
    for i in range(len(sum_list)):
        if sum_list[minidx] > sum_list[i]:
            minidx = i

    print(f'#{tc + 1} {sum_list[minidx]}')