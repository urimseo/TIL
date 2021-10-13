'''

'''

# 10진수로 바꾸는 코드
def change_to_dec(num, notation):  # 들어올 숫자(문자열로 들어온다), 진수
    tmp = 0
    for n, val in enumerate(list(map(int, num))[::-1]):   # 리스트로 변경해서 뒤집어서 사용하기
        tmp += val*(notation**n)
    return tmp

## enumerate 사용하지 않을 경우
# def change_to_dec2(num, notation):
#     tmp = 0
#     n = len(num)-1
#     for i in map(int, num):
#         tmp += i * (notation ** n)
#         n -= 1
#     return tmp


def check(num, notation):
    change_num = change_to_dec(num, notation)
    # change_num = int(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):
            if val == j: continue
            tmp = change_num - val * (notation ** n) + j * (notation ** n)

            if tmp not in binary:
                binary.append(tmp)
            else:
                return tmp

def check2():
    bi_num = 0
    for x in bi:
        bi_num = bi_num * 2 + int(x)

    for i in range(len(bi)):
        binary.append(bi_num ^ (1 << i))
    # print(binary)
    for i in range(len(tr)):
        num1 = 0
        num2 = 0
        for j in range(len(tr)):
            if i != j:
                num1 = num1*3 + int(tr[j])
                num2 = num2*3 + int(tr[j])
            else:
                num1 = num1*3 + (int(tr[j]) +1) % 3
                num2 = num2*3 + (int(tr[j]) +2) % 3

        if num1 in binary:
            return num1
        if num2 in binary:
            return num2



for tc in range(1, int(input())+1):
    bi = input()
    tr = input()
    binary = []

    print(check(bi, 2))

    # print(check2())
