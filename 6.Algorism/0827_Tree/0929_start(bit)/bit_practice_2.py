'''
비트연산 예제 3

'''

def ce(n):
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff) # 0->24, 1 -> 16, 2-> 8 3-> 0
    return p

x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)

print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
# x = 4321
p = ce(x)
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
# x = 1234
