'''
수 이어가기
'''
# num = int(input())

num = int(input())
res = []
maxlen = 0
maxlst = []
for second in range(num, 0, -1):
    res = [num]
    res.append(second)
    idx = 0
    flag = 0
    while flag != -1: # res에 0 보다 작은게 들어가는 순간 break
        for i in range(idx, idx+1):  #0 , 1, 2,
            if res[i] - res[i+1] >= 0:
                res.append(res[i] - res[i+1])
                idx += 1
            else:
                flag = -1
                break
    if len(res) > maxlen:
        maxlen = len(res)
        maxlst = res[::]

print(maxlen)
print(*maxlst)