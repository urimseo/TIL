# -*- coding: utf-8 -*-
'''
신고 횟수 제한 없음
동일한 유저에 대한 신고 횟수 1회로 처리 
k번 이상 신고된 유저는 게시판 이용 정지
해당 유저를 신고한 모든 유저에게 정지 사실 메일보냄

처리 결과 메일을 받은 유저의 메일 개수 구하기 
'''


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    reporter = {}
    count = {}
    for user in report:
        tmp = list(user.split())

        # 신고한 유저의 dict 배열 만들어 메일 보내기 -> BUT 중복 안됨 
        if tmp[1] in reporter:
            if not tmp[0] in reporter[tmp[1]]:
                reporter[tmp[1]].append(tmp[0])
                count[tmp[1]] += 1
        else:
            reporter[tmp[1]] = [tmp[0]]
            count[tmp[1]] = 1
        # 신고당한 유저의 dict로 횟수 구하기 -> 중복 안됨

    block_lst = []
    # 메일 보낼 유저들 정하기 
    for i in count:
        # 신고 당한 횟수가 정지 먹을 회수이면
        if count[i] >= k:
            # 신고자들 목록의 배열에서 
            for j in reporter[i]:
                # 각 리스트 인덱스에 메일 간 개수 더하기 
                n = id_list.index(j)
                answer[n] += 1

    # 메일 보낸 횟수 구하기 

    return answer

print(solution(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
