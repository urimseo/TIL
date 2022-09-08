'''
평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력
'''


n = int(input())

for i in range(n):
    cnt = 0
    lst = list(map(int, input().split()))
    avg = sum(lst[1:])/lst[0]
    # 맨 첫번째는 전체 lst 의 수이기 때문에 슬라이싱 하여 반복문 돌아야 한다. 
    for j in lst[1:]:
        if j > avg:
            cnt += 1
    res = cnt/lst[0] * 100
    # 소숫점 출력방법 
    print(f'{res:.3f}%')
