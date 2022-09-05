n = int(input())

# 각 자리수 나누기 
# 0보다 작을 경우  

a = n//10 # 십의자리
b = n%10 # 일의자리

res = -1 # input 값이 0부터 시작하기 때문에 변수초기화 시 0으로 하면 안됨 
flag = 0

while res != n:
  res = int(str(b) + str(a+b)[-1:])
  flag += 1

  a = res//10 # 십의자리
  b = res%10  # 일의자리

print(flag)

