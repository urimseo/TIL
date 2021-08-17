'''
N = 8, M = 4
ZYABBACD
8 4
ZYABBCCD

 # 회문이 있는지 없는지 판별
N, M = map(int, input().split())
str1 = input()
ans = 0
for i in range(N-M+1): # 회문인지 확인할 영역의 시작 인덱스
    cnt = 0
    for j in range(M//2):  # 비교 횟수, or 비교 위치->(M//2 -1)
        if str1[i+j] == str1[i+M-1-j]: # 모든 경우를 다 비교하게 됨. 일치하게되면 안쪽도 비교하기 때문..?
            cnt += 1
    if cnt == M//2: # 회문인 경우 = 비교횟수와 일치한 횟수가 같은 경우
        ans = 1
        break
print(ans)


다를경우
    for j in range(M//2):
        if str1[i+j] != str1[i+M-1-j]: # 다르면 구간 비교 중단
            break
        cnt += 1
        
    if cnt == M//2:
        ans = 1 
        break -> 만일 회문의 개수를 물어보면 ans 자체가 누적되어야 하고, break도 없어야 한다. 

'''

# 회문 자체를 출력
# 값을 따로 저장하지 않고 인덱스로 접근하는 방법
N, M = map(int, input().split()) # N - 문자열 길이, M - 회문길이
str1 = [(input()) for _ in range(N)]
for a in range(N):
    for i in range(N-M+1): # 회문인지 확인할 영역의 시작 인덱스
        cnt = 0
        for j in range(M//2):  # 비교 횟수, or 비교 위치->(M//2 -1)
            if str1[a][i+j] == str1[a][i+M-1-j]:  # 모든 경우를 다 비교하게 됨. 일치하게되면 안쪽도 비교하기 때문..?
                cnt += 1
        if cnt == M//2:  # 회문인 경우
            print(str1[a])

