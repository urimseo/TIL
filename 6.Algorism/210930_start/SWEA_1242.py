'''
암호코드 스캔

'''
# 코드 유효성 검증
def c(numlst):
    global res
    for j in range(8):
        if j % 2 == 1:  # 홀수자리합 / 검증코드
            res += numlst[j]
        else:  # 짝수
            res += numlst[j] * 3

    if res % 10 == 0:
        return res
    else:
        return 0

# 비율 찾기
def ratio(start, line):
    one = 0
    zero = 0
    lst = []
    for i in range(start, -1, -1):  # 한줄씩 찾는데 역순으로
        if line[i] == '1':  # 1을 발견하면 끝수니까.
            one += 1
            if lst and zero:
                lst.append(zero)
                zero = 0
        else:

            if one: lst.append(one)
            one = 0
            zero += 1
            if len(lst) == 3:
                break
    return min(lst)

finallst = []

res = 0
c_num = [[1, 1, 2],[1, 2, 2],[2, 2, 1],[1, 1, 4],[2, 3, 1],[1, 3, 2],[4, 1, 1],[2, 1, 3],[3, 1, 2],[2, 1, 1]] #비율 역으로3개
amho = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
N, M = map(int, input().split())
lines = set()
# 코드뽑아내기
for _ in range(N):
    temp = input().strip('0')
    if not temp: continue
    temp = bin(int(temp, 16))[2:].rstrip('0')
    lines.add(temp)
numlst = []
tmp = ''
printvalue = 0 # 최종 출력
# if len(lines) == 1:  # 코드가 하나 들어있을 경우
for line in lines:
    if len(line) <= 56:
        line = line.zfill(56)  # 56의 배수로 맞춰주기 -> 앞에 손실된 0을 추가하기
        for i in range(8):
            num = line[i*7 : i*7+7]
            numlst.append(amho[num])
        printvalue += c(numlst) # printvale
    else:
        for i in range(len(line)-1, -1, -1):
            if line[i] == '1':
                start = i
                r = ratio(start, line)  # 비율 구하기
                line = line[-56*r:] # 비율 구한만큼 잘라
                line = line.zfill(56 * r)
                origin = line[::r]
                de = -1
                for i in range(8):
                    num = origin[i * 7: i * 7 + 7]
                    numlst.append(amho[num])
                printvalue += c(numlst)  # printvale
                line = line[:-56*r].rstrip


                # 뒤의걸 잘라내고 앞에꺼 다시 탐색해야 함. -> 이 경우문제가 발생
                # 1. for 문 다시 돌려면 함수를 다시 만들어야함. 호출할 방법이 있니..?
                # 2. 분명 겹치는 구간이 존재하게 됨. 이럴 경우 어떻게 구별할건지
# if len(lines) != 1:




# start = 0  # 끝점
# lst = [] # 비율 저장
# for i in range(len(tmp) - 1, -1, -1):  # 한줄씩 찾는데 역순으로
#     if tmp[i] == '1':  # 1을 발견하면 끝수니까.
#         start = i  # 끝점을 찾아서 저장해야하는데-> 이게 계속 바뀐다. 따로 또 구해야하나..
#         break
# # 비율 찾기
# r = ratio(start)
#
# final = tmp[start - 56*r+1:start]
# # ratio2(len(final))
# de = -1


# 암호코드의 끝 점 찾기.
# 암호코드의 끝 점을 찾은 이후 -> 비율을 바로 찾자.
# 빈 배열에 비율을 저장하고, 비율이 저장되면 배열의 길이가 4가 될때까지...
# 배열에서의 최솟값이 1일 경우 1:1
# 배열의 최솟값이 배율이다.
# 그 배율만큼 56* 배율 해서 슬라이싱 하기
# 슬라이싱 한 이후 7*배율 해서 잘라보고
# 자른 만큼 다시 배율을 구해서 딕셔너리 값과 비교해서 숫자로 만들기



# 찾은 암호를 16진수 -> 2진수로 변환하는 과정
# for j in range(len(n)):
#     if n[j].isdigit():
#         num = int(n[j])
#     else:
#         num = ord(n[j]) - ord('A')+10
#
#     for i in range(3, -1, -1):
#         tmp += '1' if num & (1 << i) else '0'

# def ratio2(idx):
# # 이걸 함수로 변경하기
#     global finallst
#     one = 0
#     zero = 0
#     lst = []
#
#     for i in range(idx-1, -1, -1):  # 한줄씩 찾는데 역순으로
#         if final[i] == '1':  # 1을 발견하면 끝수니까.
#             one += 1
#             if lst and zero:
#                 lst.append(zero)
#                 zero = 0
#         elif one:
#             lst.append(one)
#             one = 0
#             zero += 1
#             if len(lst) == 3:
#                 finallst.append(lst)
#                 ratio2(idx - 7)
#                 break
#
#     return