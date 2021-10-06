def Counting_Sort(A, k):
    C = [0] * (k + 1)  # 0으로 꽉 찬 리스트
    # 정렬된 리스트가 들어갈 배열

    for a in range(len(A)):
        C[A[a]] += 1

    for v in range(1, len(C)):
        C[v] += C[v - 1]  # c[1]에 c[0] +c[1] 한다 , update

    for w in range(len(A) - 1, -1, -1):  # i가 인덱스로 들어가기 떄문에 -1하고 뒤에서부터 역순으로 0까지!
        B[C[A[w]] - 1] = A[w]  # a[i]의 값을, c의 인덱스로 가져옴 -> 그 후 정렬될 배열 B의 인덱스로 써서, a[i]넣기
        C[A[w]] -= 1  # C --

    return B


T = int(input())
for tc in range(1, T+1):
    T_num, numbers = (input().split())
    eng = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR" :4, "FIV" :5 , "SIX" :6, "SVN" :7, "EGT" :8, "NIN" :9}
    numbers = list(input().split())

    for i in range(len(numbers)):
        for j in eng.keys():
            if numbers[i] == j:
                numbers[i] = eng[j]

    B = [0] * len(numbers)
    Counting_Sort(A=numbers, k=9)

    # 정렬된 숫자 다시 바꾸기
    new = []
    for i in sorted(numbers):
        for k, v in eng.items():
            if i == v:
                a = k
                new.append(a)
    print(T_num)
    for i in new:
        print(i , end = " ")

























    #
    # def Counting_Sort(A, k):
    #     C = [0] * (k + 1)  # 0으로 꽉 찬 리스트
    #     B = [0] * len(A)  # 정렬된 리스트가 들어갈 배열
    #
    #     for a in range(len(A)):
    #         C[A[a]] += 1
    #
    #     for v in range(1, len(C)):
    #         C[v] += C[v - 1]  # c[1]에 c[0] +c[1] 한다 , update
    #
    #     for w in range(len(A) - 1, -1, -1):  # i가 인덱스로 들어가기 떄문에 -1하고 뒤에서부터 역순으로 0까지!
    #         B[C[A[w]]-1] = A[w]  # a[i]의 값을, c의 인덱스로 가져옴 -> 그 후 정렬될 배열 B의 인덱스로 써서, a[i]넣기
    #         C[A[w]] -= 1  # C --
    #
    #     return B
    #
    # Counting_Sort(A = numbers,k = 9 )
    # print(B)

    #
    # # counting sort 구현
    # def counting_sort(A, count, max):
    #
    #     # counting array 생성
    #     counting_array = [0] * (max + 1)
    #
    #     # counting array에 input array내 원소의 빈도수 담기
    #     for i in array:
    #         counting_array[i] += 1
    #
    #     # counting array 업데이트.
    #     for i in range(max):
    #         counting_array[i + 1] += counting_array[i]
    #
    #     # output array 생성
    #     output_array = [-1] * len(array)
    #
    #     # output array에 정렬하기(counting array를 참조)
    #     for i in array:
    #         output_array[counting_array[i] - 1] = i
    #         counting_array[i] -= 1
    #     return output_array


    # new = []
    # for i in sorted(numbers):
    #     for k, v in eng.items():
    #         if i == v:
    #             a = k
    #             new.append(a)
    # print(T_num)
    # for i in new:
    #     print(i , end = " ")



    # for i in range(len(numbers)-1):
    #     for j in range(i+1, len(numbers)):
    #         if numbers[i] > numbers[j]:
    #             numbers[i], numbers[j] = numbers[j], numbers[i]
    #             if numbers[i] in numbers:
    #                 new.append(numbers[i])
    # print(numbers)

    # 세번째 풀이
    T = int(input())

    for tc in range(1, T + 1):
        # 카운트 정렬용 dictionary
        dic = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
        c, n = input().split()
        arr = list(input().split())

        # dictionary의 key값과 맞으면 횟수 추가
        for num in arr:
            dic[num] += 1

        print(c)
        for key, value in dic.items():
            # 횟수만큼 출력
            for _ in range(value):
                print(key, end=' ')
        print()