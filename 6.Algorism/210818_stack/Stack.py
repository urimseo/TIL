def Stack(n):
    top = 0
    s = [0]*(n+1)
    for i in range(1,n+1):
        top += 1
        s[top] = i
        print(i)
    print(s)

    while top > 0:
        print(s[top])
        top -= 1

a = 3
Stack(a)

