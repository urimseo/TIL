'''
전기버스2


'''
## if- else 써놓으면 return
def battery(i, bat, c):
    global res
    if i == station:  # station => 까지 가야지 종점 까지 가게 된다. station -1을 하면 종점 전에 종료가 됨
        res = min(c, res)  # 교환횟수 최소값 구하기
    elif c >= res:  # 중간에 이미 최소값을 넘어가는 교환횟수가 나온다면
        return  # 멈춰!

    if lst[i] >= bat:  # 현재 충전 하려는 배터리가 현재잔량보다 많을 경우에
        battery(i + 1, lst[i] - 1, c + 1)  # 오른쪽으로 이동하고, 배터리는 -1, 교환횟수 +1
    if bat:  # 배터리가 남아있으면 충전할 필요가 없다.
        battery(i + 1, bat - 1, c)  # 그냥 이동하고, 배터리 -1, 교환횟수는 변화x


for tc in range(1, int(input()) + 1):
    lst = list(map(int, input().split())) + [0]  # 종점을 임의로 추가
    station = lst[0]
    res = station  # res는 최소값이기 때문에 최대값이 나올 수 있는 정류장 수로 초기화
    battery(2, lst[1] - 1, 0)  # 현재 위치1 -> 0은 배터리가 아니므로 제외하고 1부터 검사 / lst[1]-1 -> 시작후 한칸 갔을때 배터리잔량, c -> 교환 횟수 합할 변수
    print(f'#{tc} {res}')








# for i in range(station - 1, 0, -1):
#     left += 1
#     if left >= lst[i] + tmp:
#         c = lst.pop(i)  # 제거
#         tmp += c
#     else:
#         left = 0
#         c = 0
#         tmp = 0
#
#
# res = len(lst) - 2  # 0번-> 정류장 길이, 1번 -> default 충전기
