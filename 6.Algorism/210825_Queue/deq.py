from collections import deque
# 양방향 큐
# deq = deque()
#
# # enqueue -> append <-> appendleft (맨 앞에 붙이기)
# deq.append()
# deq.appendleft()
# # dequeue -> popleft
# deq.pop()
# deq.popleft()

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
print(*q)
while q:
    print(q.popleft())
print(q)