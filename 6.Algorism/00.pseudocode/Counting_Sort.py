"""
<카운팅 정렬>

항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여,
선형 시간에 정렬하는 효율적인 알고리즘

**제한사항**
1. 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
-> 각 항목의 발생회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트 배열 사용하기 때문
2. 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.

**시간복잡도**
O(n+k) : n은 리스트 길이, K는 정수의 최대값

**단계**
1. Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로
직접 인덱스 되는 카운트 배열(cnt)에 저장한다.
for i : 0-> N-1
cnt [Data[i]] ++

ex. cnt = list[0] * n
cnt[0] -> 0의 발생 횟수
cnt[1] -> 1의 발생 횟수 ...
...

2. 정렬된 집합에서 각 항목들 앞에 위치할 개수를 반영하기 위해 cnt의 원소를 조정한다.

-> 갯수 누적!!
                !!!이렇게 cnt 변경!!!
ex. cnt[0] = a   -> cnt[0] = a
    cnt[1] = b   -> cnt[1] = a + b         (cnt[0] + cnt[1])
    cnt[2] = c   -> cnt[2] = a + b + c     (cnt[1] + cnt[2])
    cnt[3] = d   -> cnt[3] = a + b + c + d (cnt[2] + cnt[3])

3. cnt[1]을 감소시키고 Temp에 1을 삽입한다.
-Temp -> 정렬된 배열

ex. Data(원본배열)의 마지막 인덱스의 값이 1이고, cnt[1] = 3이라면, (cnt[0] =1 이다.)
    Temp[4] 에 1 삽입 + cnt[1] 감소-> cnt[1] = 2 가 됨.

    여기서!!!
    4는 '1'의 마지막 인덱스 값,
    즉, 정렬하려는 수의 cnt 값이 Temp의 index가 된다.

"""
"""
A [] = 입력배열 (1 to k)   -> Data
B [] = 정렬된 배열         -> Temp
C [] = 카운트 배열         -> cnt
k -> 입력된 정수중 maximum 값
"""

def Counting_Sort(A, B, k):
    C = [0] * (k+1)  # 0으로 꽉 찬 리스트

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]  # c[1]에 c[0] +c[1] 한다

    for i in range(len(B)-1, -1, -1):  # i가 인덱스로 들어가기 떄문에 -1하고 뒤에서부터 역순으로 0까지!
        B[C[A[i]]] = A[i]  # a[i]의 값을, c의 인덱스로 가져옴 -> 그 후 정렬될 배열 B의 인덱스로 써서, a[i]넣기
        C[A[i]] -= 1   # C --

# 질문 -> 만약 B가 매개변수로 들어오지 않고, 함수 내부에서 선언되면..? return 값으로 못써서 안되는건가..
# 그럼 매개변수 B는 어떤 형식으로 전달이 되어야 하지...?










