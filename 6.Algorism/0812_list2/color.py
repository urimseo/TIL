# ------------
# 교수님 웹엑스 피드백 반영하여 아래 고치기
# 1. 홀수일 때 // 짝수일 때로 나누면 if와 else로 쓰기
# 2. 출력은 .join쓰지 않고 for문 돌려서 하기
# 3. 언팩하는 방법
# -------------

TC = int(input())

for tc in range(TC):
    N = int(input())
    A_list = list(map(int, input().split()))

    # A_list내 인자들과 비교의 기준이 될 max_idx, min_idx의 초기값 설정
    # max_idx = 0  #max인덱스와 min인덱스를 0 으로 해 놓으시면... 두번째 영역이면, / 구간이 바뀌면 그 다음에 초기화되어야 함
    # min_idx = 0  #여기서 초기화를 시작하면 무조건 맨 앞에있는 애와 초기화가 됨
    # 구간이 정해지고 나면 맨 앞에서 초기화를 해야 함.
    # 그래서 초기화 위치가 여기가 아니라 'for i부분 열고, 그 시작부분'
    for i in range(0, len(A_list) - 1):  # 10번만 비교영역을 좁혀나가면 됨(인덱스 기준 range설정)
        # ------대분류: i가 0/짝수번 인덱스에 들어갈 값을 찾을 때, 그 값은 max값
        max_idx = i
        min_idx = i
        if i % 2 == 0:
            for j in range(i + 1, len(A_list)):  # 자기자신과 비교할 필요는 없으니
                if A_list[max_idx] < A_list[j]:
                    max_idx = j
            # print(max_idx)
            A_list[i], A_list[max_idx] = A_list[max_idx], A_list[
                i]  ##현재 값을 원하는 i번째 인덱스 값을 A_list내 max_idx자리에 위치한 값으로 바꿔줌
        # ------대분류: i가 홀수번 인덱스에 들어갈 값을 찾을 때, 그 값은 min값
        # min_idx = i
        else:
            for j in range(i + 1, len(A_list)):  # len(A_list)는 20이면, 인덱스상으로는 19까지 있음.
                if A_list[min_idx] > A_list[j]:
                    min_idx = j  # 이렇게 리스트 끝까지 점검하며 계속 바꿔주다가
            # 리스트 내 j, 즉, i의 출발시점부터 리스트 끝까지 봤을 때 결정된 최종 min_idx
            # print(min_idx)
            # 단, 이 위치는 여전히 이 문제의 큰 대분류인 if i%2 != 0내에서 봐야
            A_list[i], A_list[min_idx] = A_list[min_idx], A_list[
                i]  # 현재 값을 원하는 i번째 인덱스 값을 A_list내 min_idx자리에 위치한 값으로 바꿔줌
    print(f'#{tc + 1}', end=' ')

    for i in range(10):  # A_list에서 0부터 9까지의 인덱스에 위치한 값만 뽑기
        print(A_list[i], end=' ')
    print()  # 이걸 안써주면 다음 N인풋(10,20)이 위에 end = ' '에 붙어서 같이나와버림.

    # print(' '.join(map(str, A_list[:10])))