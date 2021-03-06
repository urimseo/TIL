"""
<버블 정렬>

인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

**단계**
1. 첫번쨰 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
2. 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
3. 교환하며 자리를 이동하는 모습이 거품 같다고 하여 거품 정렬이라함.

원소의 수 = N
구간의 끝 = i
인접 원소의 왼쪽 = j
j = i-1 일때까지 반복 (인접원소의 마지막 2개중 왼쪽 원소이기 때문!)

** 시간복잡도 **
O(n^2)
"""


# 슈도코드

def Bubblesort(a):
    for i in range(len(a) - 1, 0, -1):  # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# 예시 배열
a = [7, 3, 2, 4, 5]
print(Bubblesort(a))

