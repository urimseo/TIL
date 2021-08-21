C = 0
# arr = [i for i in range(C)]
subset = [[]] # size = 1
arr = [3, 6, 7, 1, 5, 4]
for num in arr:
    size  = len(subset)
    for y in range(size):
        subset.append(subset[y] + [num])


# lst = [1, 2, 3, 4]
# n = len(lst)
# total = []
# for i in range(1, 1<<n):
#     arr = []
#     for j in range(n):
#         if i & (1<<j):
#             arr.append(lst[j])
#     total.append(arr)
#
# print(total)