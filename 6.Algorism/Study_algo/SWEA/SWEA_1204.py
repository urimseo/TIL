'''
최빈수 구하기
- 학생의 수는 1000명
- 최빈수가 여러개일 때에는 가장 큰 점수를 출력
- 빈 스택 만들어서 집어넣기 0 ~ 100 까지 필요하니까 101개
- idx 값을 성적으로 매겨서 값 +1
- 여기서 최빈수중 큰 값을 찾기

'''

for tc in range(1, int(input())+1):
    n = int(input())
    score = list(map(int, input().split()))
    mode = [0] * 101
    for i in score:
        mode[i] += 1

    modeV = 0  # 최빈수인 점수
    idx = 0  # 최빈수
    for k in range(len(mode)):
        tmp = mode[k] # 현재 빈도수
        if tmp >= idx:  # 현재 빈도수와 최빈수 비교
            idx = mode[k] # 최빈수
            modeV = k  # 최빈수 점수


    print(f'#{n} {modeV}')

