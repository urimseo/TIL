# T = int(input())
#
# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     charge = list(map(int, input().split()))
#     bus_stop = [0] * N
#
#     # 충전기가 있는 정류장에 1로 표시
#     for i in charge:
#         bus_stop[i] += 1
#
#     count = 0  # 충전 횟수
#     bus_pos = 0  # 버스 위치
#
#     while True:
#         bus_pos += K  # 버스의 위치 K만큼 이동
#
#         if bus_pos >= N:  # 종료 조건 설정 (버스 위치가 정류장 넘어가면 종료)
#             break      # 첫번쨰 -> 3 2 1 0
#         for i in range(bus_pos, bus_pos - K, -1):  # 버스 위치에서 백스탭으로 정거장 있는지 확인
#             if bus_stop[i]:  # 충전소 있다면 버스 위치를 정류장으로 옮김.
#                 count += 1
#                 bus_pos = i
#                 break
#         else:
#             count = 0
#             break
#
#     print(f'#{tc} {count}')
# #
#






T = int(input())

for case in range(T):
    k, n, m = map(int, input().split())
    bus = list(map(int, input().split()))
    # n: 끝 k: 이동 m:충전기
    lst = [0] * (n + 1)
    for i in bus:
        lst[i] = 1 # 0000 에다가 정류장 위치는 1
    i = 0 # 버스 위치
    cnt = 0 # 충전횟수
    while i < n - k:  # 버스 위치가 총 졍류장 수 넘어가면 (도착!)
        for j in range(k):  # 0  k- 이동하는 수
            if lst[i + k - j] == 1:
                i = i + k - j
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{case + 1} {cnt}')

