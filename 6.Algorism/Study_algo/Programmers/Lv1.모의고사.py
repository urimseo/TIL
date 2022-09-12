def solution(answers):
    answer = []
    A = [1, 2, 3, 4, 5] * 2000
    B = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    score = [0, 0, 0]
    for i in range(len(answers)):
        if A[i] == answers[i]:
            score[0] += 1
        if B[i] == answers[i]:
            score[1] += 1
        if C[i] == answers[i]:
            score[2] += 1
    mx = max(score)
    
    for i in range(3):
        if mx == score[i]:
            answer.append(i+1)
    return answer

print(solution([1, 2, 3, 4, 5]))