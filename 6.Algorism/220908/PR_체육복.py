'''
체육복 빌려주기 
수업을 들을 수 있는 학생의 최댓값 구하기 
'''


def solution2(n, lost, reserve):
    answer = 0
    lst = [1 for _ in range(n+2)]

    for i in reserve:
        lst[i] = 2


    for j in lost:
        lst[j] -= 1

    for k in range(1,n+1):
        if lst[k] == 0:
            if lst[k-1] == 2:
                lst[k] = 1
                lst[k-1] = 1
            elif lst[k+1] == 2:
                lst[k+1] = 1
                lst[k] = 1

    for x in range(1, n+1):
        if lst[x] >= 1:
            answer += 1

    return answer


print(solution2(5,[2, 4],[1]))



def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i-1)
        elif i + 1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)

print(solution(5,[2, 4],[3]))