# 가장 긴 회문을 구하는 문제
# 100*100 arr이므로, M의 길이가 100인 회문이 있나 먼저 점검
# 없으면, 점검 구간을 줄여감
# M이 0이 되면 while문 중단
# while M >= 1이면 while문이 돌아가도록 함

for tc in range(10):
    T = int(input())  # 시행착오
    arr = [input() for _ in range(100)]

    # ------시행착오
    # while안에 for i와 for j모두 넣고 for i forj 모두 돈 후 M길이 회문이 없으면, 그때 M을 하나 줄이도록

    flag = True

    # while을 사용해보기.
    # 인덱스로 바로 접근해보기.
    M = 100
    while True:
        # 1. while 종료조건1
        if not flag:  # while문 나올 break(다음 tc가기 위함)
            break
        # 2 while 종료조건2
        if M == 0:
            break

        # 1. arr형성
        for i in range(100):
            # i, j 지점 찍기 #는 일단 M길이에 상관없이 모두 봐야 함. for i in range(N-M+1)을 하게 되면 회문의 길이가 100인 경우, for문이 1번만 돌고 끝남.
            if not flag:  # 한번이라도 회문이 발견되어 아래 while문에서 여기로 반영되면, for i문도 멈춰서 다음 tc로 갈 수있도록 while문 까지 접근
                break
            # 이 for j안 M은 계속 변함. while문 안에서 for문의 범위가 조정됨.
            # j의 범위는 계속 조정될 것, M(100부터)의 길이를 만족하는 회문이 없을 시 1씩 줄어가면서
            for j in range(100 - M + 1):  # M만큼의 길이가 남을 때까지만만. 회문점검의 시작위치 증가.

                # i와 j점이 정해졌으니, 시작위치 바로 정함./비교범위 내 회문 바로 확인하기.
                # j는 range(8-8+1) = 0  --> range(8-7+1) = 0, 1 --> 이런식으로
                cnt1 = 0
                cnt2 = 0
                for k in range(M // 2):
                    if arr[i][j + k] == arr[i][j + M - 1 - k]:  # 가로방향으로 더함  #1차원에서 썼던 i,j대신 j,k를 쓰는 것
                        cnt1 += 1
                    if arr[j + k][i] == arr[j + M - 1 - k][i]:  # 1차원에서 썼던 i,j대신 j,k를 쓰는 것
                        cnt2 += 1
                # --
                # 이 시점에서 cnt1과 cnt2가 나옴.
                if (cnt1 == M // 2) or (cnt2 == M // 2):  # 회문점검횟수와 페어의 수가 같으면 -->회문임
                    print(
                        f'#{tc + 1} {M}')  # 회문의 길이는, while문이 끝났을 때의 M, (M이 홀수냐 짝수냐에 따라서 cnt1*2 거나 cnt1*2+1이기도 할텐데. 이건 복잡하니까.!)
                    # 같은 i,j시점간 같은 길이의 회문(M)간 비교이므로, or을 쓸 수 있을 것.
                    flag = False
                    # ---여기서, 출력하고 바로 break.(이 tc의 경우는 끝남 ->1.break으로 for j나오고, 2.while과 3. for i까지 나오는 것도 flag로 조정)

                    break  # j for문 나옴.

        # 구간을 '다' 돌아서 'i&j' for문이 끝났거나, 중간에 break이 없어서 while이 한번 더 돌아야 한다면, M에서 1씩 빼줄 것(M이 0되면 while에서 나가도록/while종료조건으로 설정)
        M -= 1

    # while완전 종료 시, 사실 문제에서는 종료시 무엇을 출력하라는 언급은 안했으므로, M=0이 되어 저절로 종료하여 다음 tc로 갈 것 같다.