
t = int(input())
for tc in range(t):
    test, lenlst = input().split()
    print(test)
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    lst = list((input().split()))
    count = [0] * 10
    for i in lst:
        for j in range(10):
            if i == num[j]:
                count[j] += 1
    for i in range(10):
        for j in range(count[i]):
                print(num[i], end =' ')