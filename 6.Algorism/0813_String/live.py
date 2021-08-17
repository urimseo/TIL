# s = list(input())
# n = len(s)
# for i in range(n//2):  # [s-1-i]
#     s[i], s[(i+1)* -1] = s[(i+1)* -1], s[i]  # abcdef  a012345  0 -> -1 1 -> -2 2 -> -3
# print(s)

# cnt = [0] *26
# s = 'aba'
# for x in s:
#     cnt[ord(x) - ord('a')] += 1  # 98 - 97 -> 1 #
# print(cnt)
#
#
# print(chr(65))


def atoi(s):  # s에 '123'
    i = 0
    for x in s:
        i = i * 10 + (ord(x) - ord('0')) # int(x)

    return i

def my_itoa(i):
    s = ''
    while i > 0:
        s += chr(i % 10 + ord('0'))
        i //= 10
    s = s[::-1]
    return s


a = '123'
b = atoi(a)
print(b)

c = 456
print(my_itoa(c))

