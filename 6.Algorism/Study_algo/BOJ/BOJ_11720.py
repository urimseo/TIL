'''
숫자의 합
'''

n = int(input())

print(sum(map(int, input()))) 

# for문 이용
nums = input()
total = 0

# 1
for i in nums:
    total += int(i)
print(total)

# 2

for i in range(n):
    total += int(nums[i])
print(total)

