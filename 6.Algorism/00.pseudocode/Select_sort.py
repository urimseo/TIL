'''
<선택정렬>

주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

**정렬과정**
1. 주어진 리스트 중에서 최소값을 찾는다 -> 전체 구간
2. 그 값을 맨 앞에 위치한 값과 교환한다.
3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

**시간복잡도**
O(n^2)
'''

def selectionSort(a):
    for i in range(len(a)-1):
        min = i  # i는 0 부터 len(a) 까지 들어감
        for j in range(i+1, len(a)):
            if a[min] > a[j]: # 처음 비교는 a의 0번쨰 인덱스와, a의 1번 인덱스로 비교
                min = j
        a[i], a[min] = a[min], a[i]
    return a

arr = [3, 5, 7, 1, 2]
print(selectionSort(arr))