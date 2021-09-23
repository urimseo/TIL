def check(num):  # 단조 증가 판단
    number = list(str(num))
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    res = -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            num = nums[i] * nums[j]
            if num <= res:
                continue

            if check(num) and res < num:  # 단조 증가이면서 값이 더 큰 경우 변환
                res = num
    print(f'#{tc} {res}')

'''
for tc in range(1, int(input())+1):
    n = int(input())
    lst = list(map(int, input().split()))

    increase = []
    #Ai*Aj 만들기
    for a in range(n-1):
        for b in range(a+1, n):
            increase.append(str(lst[a]*lst[b]))
    # print(increase)
    final = []
    for s in range(len(increase)):
        # tmp = []
        # tmp.extend(increase[s]) # tmp는 str 형태로 한글자씩 나눠서 들어감
        flag = 1
        tmp_num = increase[s]
        for i in range(len(tmp_num)-1): # 하나의 숫자에서
            if tmp_num[i] > tmp_num[i+1]: # 단조 증가인것
                flag = 0
        # 단조 증가가 아니면..
        if flag == 1 or len(tmp_num) == 1:  # 단조 증가거나, 한자리수이면
            final.append(int(tmp_num)) # 새로 리스트에 저장

        else: # 다음 숫자로 넘어감
            continue
    # print(max(final))
    if not final:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(final)}')
'''

