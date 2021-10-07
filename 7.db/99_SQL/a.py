import heapq

a = [1, 3, 5, 2, 4]
b = []
# for num in a:
#     heapq.heappush(b, (-num, num))
# print(b)


heapq.heapify(a)
print(a)
#
heapq.heappush(a, 8)
print(a)

# heapq.heappop(a)



## 우선순위 조건 걸어서 출력
# A = [(1, 2), (3, 1), (5, 5), (2, 2), (3, 3)]
# for num in a:
#     heapq.heappush(b, num[1], num[0])   # 첫번째 우선순위가 num[1], 두번쨰가 우선순위 2
# print(b)
# while b:
#     n1, n0 = heapq.heappop(b)
#     print((n0, n1))