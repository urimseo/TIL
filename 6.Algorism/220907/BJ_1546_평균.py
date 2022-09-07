'''
최댓값 = M
모든 점수/M * 100 로 변경
그 후 새로운 평균 구하기 
'''

n = int(input())
score = list(map(int, input().split()))

max_s = max(score)
for i in range(n):
    k = score[i]
    score[i] = k/max_s*100

print(sum(score)/n)