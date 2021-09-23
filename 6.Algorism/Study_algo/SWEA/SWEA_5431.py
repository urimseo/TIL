for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))
    student = [i for i in range(1, n+1)]

    for i in submit:
        if i in student:
            student.remove(i)

    print('#{}'.format(tc), end=' ')
    print(*student)