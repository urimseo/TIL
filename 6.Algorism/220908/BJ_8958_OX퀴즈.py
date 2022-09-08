'''
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램
'''

tc = int(input())

for _ in range(tc):
    n = input()
    score = list(n)
    res = 0
    k = 0
    for i in score:
        if i == "O":
            k += 1
            res += k
        else:
            k = 0
    print(res)


'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

10
9
7
55
30
'''