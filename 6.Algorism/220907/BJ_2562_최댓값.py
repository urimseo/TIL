'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성
'''
max_num = 0
cnt = 0
flag = 0
for i in range(9):
    k = int(input())
    flag += 1
    if k > max_num:
        max_num = k 
        cnt += flag
        flag = 0

print(max_num)
print(cnt)