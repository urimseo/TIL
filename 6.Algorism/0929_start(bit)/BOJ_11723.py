'''
피자의 20가지 토핑
add
remove
check :
toggle : 1->0, 0->1
all : 모두 0으로 만들기
empty -> 토핑 모두 제거 : 모두 0으로 만들기

비트 -> 총 20개 만들어야함.
1<<20
but 우리는 21개 만들거임
-> (1<<21)개로 만든 후에 0번째 칸 사용 안함
b21 ~~~ b0


# watch 창에 bin(S)[2:] -> str
# list(bin(S)[2:]) 이거 등록하고 디버깅하기
'''

import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline()) # 명령어의 개수 (빠른입력)
S = 1 << 21  # 비트 집합
de = -1  # 디버깅 포인트

for _ in range(N):
    temp = sys.stdin.readline().split()
    if len(temp) == 2:
        cmd, x = temp[0], int(temp[1])  # 튜플 -> unpacking 해서 cmd랑 x에 넣음
    else:
        cmd = temp[0]

    if cmd == "add":
        S |= (1 << x)  # or 연산 = x번쨰 bit 와 or 연산 하게된다.
    elif cmd == "remove":
        S &= ~(1 << x)  # not 연산을 적용
        # if S & (1 << x):
        #     S ^= (1 << x)  # xor 연산 1 ^ 1 -> 0
        # else:
        #     continue

    elif cmd == "check":
        print((S & (1 << x)) >> x)
        # if S & (1 << x):
        #     print(1)
        # else:
        #     print(0)
    elif cmd == "toggle":
        S ^= (1 << x)
    elif cmd == "all":
        S = (1 << 20) - 1 # -1을 할 경우 전부 뒤집힌다. ??
    elif cmd == "empty":
        S = (1 << 21)

'''
import sys
sys.stdin = open("input.txt","r")
N = int(sys.stdin.readline()) # 명령어 개수  , sys.stdin.readline() -> 빠른입력
S = 1 << 21
for _ in range(N):
    temp = sys.stdin.readline().split()
    if len(temp) == 2:
        cmd, x = temp[0], int(temp[1])
    else :
        cmd = temp[0]
    de = -1
    if cmd == "add":
        S |= (1 << x) # x 번째 bit와 or 연산
    elif cmd == "remove":
        S &= ~(1 << x)
    elif cmd == "check":
        print((S & (1 << x)) >> x)
    elif cmd == "toggle":
        S ^= (1 << x)
    elif cmd == "all":
        S = ((1 << 21) - 1)
    elif cmd == "empty":
        S = (1 << 21)
'''