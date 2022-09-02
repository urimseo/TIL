def solution(lottos, win_nums):
    answer = []  # [최고순위, 최저순위]

    remove = 0 # 지워진 글자수 -> 최고등수 매기기 
    match = 7 # 일치하는 횟수 (등수 계산) -> 최저 등수 매기기
    for i in lottos:
        if i == 0:
            remove += 1
        for j in win_nums:
            # 최저 순위 구하기
            if i == j:
                match -= 1
                break

    # 최저순위에서 지워진 글자만큼 맞았다고 가정 하고 순위 높이기 
    if match > 6: 
        # 지워진 글자가 하나라도 있을 경우
        answer = [match-remove, 6]
        # 전부 일치하지 않을 경우 
        if match > 6 and remove == 0:
            answer = [6, 6]
    else:
        answer = [match-remove, match]

    return answer

solution([44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]) # [3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]