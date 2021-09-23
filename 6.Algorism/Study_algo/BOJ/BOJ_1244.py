'''
스위치 켜고 끄기
'''
n = int(input()) # 스위치의 개수
switch = [0] + list(map(int, input().split()))  # 스위치의 상태
num = int(input()) # 학생수
stu = [list(map(int, input().split())) for _ in range(num)]
for s in stu:  # 리스트 하나하나 가져오기
    flag = 0
    flag2 = 0
    if s[0] == 1:  # 남학생
        a = 1
        while flag == 0: # 인덱스 범위 넘어가면 종료
            if s[1]*a <= n:
                if switch[s[1] * a] == 1:  # 해당하는 배수
                    switch[s[1] * a] = 0
                else:
                    switch[s[1] * a] = 1
                a += 1
            else: # 배수가 인덱스 넘어감
                flag = -1
                break

    else:
        if s[0] == 2: # 여학생
            if switch[s[1]] == 1:  # 일단 중간지점은 바뀜
                switch[s[1]] = 0
            else:
                switch[s[1]] = 1

            idx = s[1]
            section = 1
            while flag2 == 0:  # 인덱스 벗어나면 -1
                if idx-section > 0 and idx+section <= n:
                    left = idx - section  # 왼쪽
                    right = idx + section  # 오른쪽 지정하고
                    section += 1 #다음 섹션 늘릴 준비
                    if switch[left] == switch[right]:
                        if switch[left] == 1:  # 같으면 바꿔
                            switch[left] = 0
                            switch[right] = 0
                        else:
                            switch[left] = 1
                            switch[right] = 1
                    else: # 왼쪽 오른쪽 달라도 끝
                        flag2 = -1
                        break
                else:
                    flag2 = -1
                    break

switch.pop(0)
if n > 20:
    for i in range(n//20):
        print(' '.join(list(map(str,switch[20*i:20*i+20]))))
    print(' '.join(list(map(str, switch[20*i + 20:]))))
else:
    print(*switch)


# if len(switch) <= 20:
#     print(*switch[0:21])
# elif len(switch) <= 40:
#     print(*switch[0:21])
#     print(*switch[21:41])
# elif len(switch) <= 60:
#     print(*switch[0:21])
#     print(*switch[21:41])
#     print(*switch[41:61])
# elif len(switch) <= 80:
#     print(*switch[0:21])
#     print(*switch[21:41])
#     print(*switch[41:61])
#     print(*switch[61:81])
# else:
#     print(*switch[0:21])
#     print(*switch[21:41])
#     print(*switch[41:61])
#     print(*switch[61:81])
#     print(*switch[81:101])



