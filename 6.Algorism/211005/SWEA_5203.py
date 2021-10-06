'''
베이비진
선수 A, B 가 번갈아가면서 나눠가진다.


def f(lst):
    global flag
    if max(lst) >= 3:
        flag = 1
        return flag
    for j in range(len(lst)-2):
        # triplet 검사
        if lst[j] >= 1 and lst[j+1] >= 1 and lst[j+2] >= 1:
            flag = 1
            return flag

for tc in range(1, int(input())+1):
    card = list(map(int, input().split()))
    A = [0]*10
    B = [0]*10
    flag = 0
    winner = 0
    for i in range(12):
        if flag: break
        if i % 2 == 0:
            A[card[i]] += 1
            if i >= 5:
                if f(A):
                    winner = 1
                    break
        else:
            B[card[i]] += 1
            if i >= 6:
                if f(B):
                    winner = 2
                    break
    print(f'#{tc} {winner}')

'''
def is_run(num, card):
    if num -2 >= 0:
        if card[num-2] and card[num-1] and card[num]:
            return True
    if num -1 > 0 and num + 1 < 10:
        if card[num - 1] and card[num + 1] and card[num]:
            return True
    if num +2 < 10:
        if card[num] and card[num+1] and card[num+2]:
            return True

for tc in range(1, int(input())+1):
    card1 = [0]*10
    card2 = [0]*10
    lst = list(map(int, input().split()))
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            card1[lst[i]] += 1
            # triplet 검사와 run 검사
            if card1[lst[i]] >= 3:
                winner = 1
                break
            if is_run(lst[i], card1):
                winner = 1
                break
        else:
            card2[lst[i]] += 1
            if card2[lst[i]] >= 3:
                winner = 2
                break
            if is_run(lst[i], card2):
                winner = 2
                break
    print(f'#{tc} {winner}')