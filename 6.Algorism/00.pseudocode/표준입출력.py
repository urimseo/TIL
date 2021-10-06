
##1##
'''
a = 3.14159265

print(a)
print('%.4f'%a)
print(f'{a:.4f}')  # 소수점 아래자리수 제한 -> 반올림 되어 처리됨
print(f'{a:6.4f}')  # 전체자리수 제한
'''
##2##
'''
1
5 10
0000000000
0123456789
0000000000
0000000000
0000000000
'''
'''
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    # arr = [input() for _ in range(N)]
    # print(arr)
    # ['0000000000', '0123456789', '0000000000', '0000000000', '0000000000']
    # -> 문자열은 수정이 안됨

    # arr2 = [list(map(int, input())) for _ in range(N)]
    # print(arr2)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # arr2[1][2] = 3
    # print(arr2[1][2]) -> 2에서 3으로 변경됨됨

   # arr3 = [list(input()) for _ in range(N)]
    # print(arr3)
    # ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
'''

##3##
import sys

sys.stdin = open("input.txt", "r")
sys.stout = open("output.txt", "w")
text = input()
print(text)
  

