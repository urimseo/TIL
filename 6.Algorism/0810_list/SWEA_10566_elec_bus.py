T = int(input())

for tc in range(T):
    Kilo, Station, Charger = map(int, input().split())
    C_li = list(map(int, input().split()))
    # Kilo = 한번 이동 가능 구간, Station - 총 정류장 수 , Charger - 충전소
    # 충전횟수
    count = 0
    for i in range(Station+1):  # 정류장 끝까지 확인 [0 1 2 3 4 5 7 8 9 10]

        # 충전기 간격 kilo 보다 크면 0 출력
        for x in range(Charger - 1):
            if C_li[0] > Kilo or C_li[x + 1] - C_li[x] > Kilo:
                count = 0

        for j in range(Charger):  # [1,3,5,7,9]
            # 처음 만났을때
            if j == 0 and i == C_li[j]:
                if C_li[1] > Kilo:  # 처음 만난 충전소가
                    count += 1


            # 그 외 중간의 충전소 [1 3 5 7 9]
            elif j != 0 and j != (Charger-1) and i == C_li[j]:
                if C_li[j+1] - C_li[j-1] > Kilo:


                    '''
                    1개만 주유 안하는걸 거침. 좀 더 작은 범위의 구간을 가려내지 못한다. 
                    그 전에 주유소에서 주유를 했다는 걸 가정하고 다음 주유 구간 찾음.
                    C_li[j] - C_li[j-1]
                    C_li[j+1] -C_li[j] 
                    '''

                    count += 1

            # 마지막 충전소 일때
            elif j == (Charger-1) and i == C_li[j]:
                if Station - C_li[j-1] > Kilo:
                    count += 1

    print(f'#{tc+1} {count}')

    # 이렇게 할 경우 테스트케이스 전체 통과 안됨.



    '''
     i => 0 1 2 3 4 5 6 7 8 9 10

     Cli -> 1 3 5 7 9    
     j -> 0 1 2 3 4
     
     i =1, j = 0(1) 일때 정류소에서 만난다. 
     얼만큼 이동했는지가 중요한데,
     j [0] 이면 사실 처음 만난거니까 -> 그 다음 j[1] 의 값이랑 j[0]을 뺀 값 + j[0]에 들어있는 값을 더해서 3이 넘지 않으면 충전하지 않아도 된다.
     
     
     첫번째 시작점과 종점을 충전기에 붙여서 비교하면 특수 case 만들지 않고, 한번의 반복으로 가능하다.
    '''







        # for j in C_li :
        #     if C_li[j+1] - C_li[j] > Kilo:
        #         print(f'#{T+1} 0')


