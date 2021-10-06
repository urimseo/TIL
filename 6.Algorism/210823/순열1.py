def f(i, N):
    if i == N:
        print(p)

    else:
        for j in range(i, N): # p[i] <-> p[j]  자리 교환
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]
p = [1, 2, 3]
f(0, 3)