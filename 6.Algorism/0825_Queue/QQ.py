def enq(data):
    global qsize
    global rear
    global front
    if (rear+1) % qsize == front:
        # print('Full')  # 꽉 찼으면 다찼다고 표시
        front = (front+1) % qsize  # 다 찼으면 다시 덮어쓰기위해 front를 하나 올림.
        # front를 하나 올리는 이유는 front가 처음걸 가리키니까, 처음 위치를 옮기고 rear를 넣어야함.
    else:
        rear = (rear +1 % qsize)
        q[rear] = data


front, rear = 0, 0
qsize = 4
q = [0] * qsize

enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
while front != rear:
    front = (front+1) % qsize
    print(q[front])