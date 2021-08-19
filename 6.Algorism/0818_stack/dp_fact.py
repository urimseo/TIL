def fact(n):
    table[0] = 1
    for i in range(1, n + 1):
        table[i] = i * table[i - 1]

    return table[n]


n = int(input())
table = [0] * (n + 1)
print(fact(n))

#  함수 호출복귀하는 시간이 줄어듬.
# 1. 공식 찾기
# 2. 재귀, 혹은 단순 반복으로 구현
# 3. 메모이제이션으로 바꿔보기
# 4. dp로 변경해보기 