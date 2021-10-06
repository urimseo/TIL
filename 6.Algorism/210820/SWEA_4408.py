'''
자기 방으로 돌아가기
- 겹치는 구간에서는 한사람만 이동 가능
- 거리와 시간은 상관 없음
- 최소 이동단위시간 구하기

1. 카운트 배열
2. 지나가야할 곳을 전부 카운트
3. 기본은 time = 1
3. 겹치면 time ++

'''
T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 돌아갈 사람의 수
    student = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(2):
            student[i][j] = (student[i][j] +1) //2 #지나치는 복도로 저장

    corr = [0]*201

    for i in range(n): # 역으로 오는 방향 변경하기
        if student[i][0] > student[i][1]:
            student[i][0], student[i][1] = student[i][1], student[i][0]

        for j in range(student[i][0], student[i][1]+1):  # 카운팅
            corr[j] += 1
    # 가장 큰수 찾기
    time = 0
    for i in corr:
        if i > time:
            time = i

    print(f'#{tc} {time}')



'''
#지나치는 복도로 저장
student = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(2):
        student[i][j] = (student[i][j] +1) //2 
        
-> 함수로 가능
# map 활용해서 input 받을때 함수 호출 
student = [list(map(div, input().split())) for _ in range(n)]

def div(num):
    return (int(num)+1)//2

**직접 함수를 만들어서 사용 가능**
map(int -> div로 변경하여 함수를 호출하고 
input 받는 숫자를 div의 매개변수 num으로 받아온다. 
그냥 input을 받으면 str이기 때문에 int로 형변환
지나치는 복도로 저장하기 위해서 +1 //2 를 해준다. 
'''

