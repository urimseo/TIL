

words = input()
i = 0
size = 0
croatia_alphabet = ['c=', 'c-', 'dz=','d-', 'lj', 'nj', 's=', 'z=']

while len(words) > 0:
    temp = words[0:i]
    if temp in croatia_alphabet:
        words = words[i:]
        size += 1
        i = 0

    elif i > len(words):
        words = words[1:]
        size += 1
        i = 0

    else: i += 1

print(size)





'''
chars = input()
i = 0
total = 0
while i < len(chars)-1:
    if chars[i]+chars[i+1] in ('lj', 'nj') or chars[i+1] in ('-', '='):
        i += 1
    elif chars[i:i+3] == 'dz=':
        i += 2
    total += 1
    i += 1
if i == len(chars)-1 and 97 <= ord(chars[i]) <= 122:
    total += 1
print(total)

'''



# c_alpha = ['c=', 'c-', 'dz=', 'd-','lj', 'nj', 's=', 'z=']
#
# text = input()
#
# # alpha를 가리키는 인덱스
# # text를 가리키는 인덱스 따로 지정해야한다.
# # alpha에 있는첫번째 값이랑 c에 있는 값이 같다면..+= 1
# res = len(text)
# t = 0
# while t < len(text):
#     flag = 0
#     for c in c_alpha:
#         if flag != 0:
#             break
#         else:
#             if text[t] == c[0]:
#                 cnt = 1
#                 while cnt != 0:
#                     for i in range(1, len(c)):
#                         if text[t+i] == c[i]:
#                             cnt += 1
#                             if cnt == len(c):
#                                 res -= (len(c) - 1)
#                                 cnt = 0
#                                 t += len(c)
#                                 flag = 1
#                                 break
#                         else:
#                             cnt = 0
#                             break
#     else:
#         if flag == 0:
#             t += 1
# print(res)






