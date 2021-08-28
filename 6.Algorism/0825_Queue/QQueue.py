Q = [0] * 100

front, rear = -1, -1

rear += 1
Q[rear] = 1 # enQueue(1)

rear += 1
Q[rear] = 2  # enQueue(2)

rear += 1
Q[rear] = 3  # enQueue(3)

while front != rear:  # print(deQueue())
    print(Q[front], end=' ')


listQ = []
listQ.append(1)  # append는 시간이 오래걸림. 새로 리스트를 복사해서 만들고 추가하기 때문
listQ.append(2)
listQ.append(3)
while listQ:
    print((listQ.pop(0)), end = ' ')
print()