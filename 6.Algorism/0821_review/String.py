for tc in range(10):
    tcase = int(input())
    ptrn = input()
    text = input()
    p = len(ptrn)
    t = len(text)
    cnt = 0
    for i in range(t-p+1):
        if text[i:i+p] == ptrn:
            cnt += 1
    print(f'#{tcase} {cnt}')
