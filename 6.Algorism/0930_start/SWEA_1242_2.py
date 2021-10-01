'''
암호코드 스캔
1. 0제거
- line 별로 읽을때 .strip('0)
입력을 받으면서 strip 하기
2. 라인별로 strip 한 걸 가져와서 2 진수로 바꾸고
unique 한 원소들만 집어넣을 수있는 set
lines = set()
-> lines 에 strip을 한게 나오게 된다.

'''
import sys
sys.stdin = open("input.txt", "r")

amho = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    lines = set()
    # 코드뽑아내기
    for _ in range(N):
        temp = input().strip('0')
        if not temp: continue
        temp = bin(int(temp, 16))[2:].rstrip('0')
        lines.add(temp)

    for line in lines:
        line = line.zfill(56)  #56의 배수로 맞춰주기 -> 앞에 손실된 0을 추가하기
        print(tc)
        print(line)
# 1100101000110100011010111101101110010011001001101110110000000000000000000000000000000110010110111010111100010110100011000101101100010101111
# 처음에 56개를 보고, 코드가 만들어졌는지 확인하기 -> 코드가 만들어졌다?? ->이 과정을 함수로 뺴기
# line = s[-56:]
# is_valid(line) # 끝에서부터 56개를 가져와라
# 실패 -> 다음사이즈를 검사하기 *2
# line = s[-56*2] ... 3배, 4배 등... 진행하기

#찾게 되면 이걸 지워야한다.
# line = [:-56*size].rstrip

