T = int(input())

for tc in range(1, T + 1):
    x, N = input().split()
    N = int(N) # len(numbers)
    numbers = input().split()

    number_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count_list = [0] * 10

    for i in range(10): # 숫자 수 0 ~ 9
        for j in range(N): #7024
            if number_list[i] == numbers[j]:
                count_list[i] += 1 # 빈 리스트(중간 숫자개수만 들어가있는것)

    print(f'#{tc}')
    for k in range(10): # 0 ~ 9
        num = number_list[k] + " "
        print(num * count_list[k], end='')
    print()