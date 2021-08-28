'''
# q에 들어오면 append..?

'''
chew = 20 # 마이쭈 개수
q = []
cnt = [0] * (chew+1) # 사람이 받은 수 세기
p = 1 # 처음 줄 서는 사람
v = 0 # 받을사람
while chew > 0:
    q.append(p)
    cnt[p] += 1
    v = q.pop(0) # 현재 받은 사람은 v임.
    chew -= cnt[v]  # 준만큼 전체마이쮸에서 빼기

    q.append(v) # 받은사람이 다시 바로 줄서고
    cnt[v] += 1 # 받을 개수
    p += 1 # 다음 사람 따라들어가고
    # for i in range(1, p): # 따라 들어갈 사람은 계속 증가해서

print(v)

