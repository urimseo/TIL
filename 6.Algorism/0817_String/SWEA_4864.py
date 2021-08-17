'''
<고지식한 패턴검색 -> 강의안>
T = int(input())
for tc in range(1,T+1):
    pattern = input()  # j
    text= input()  # i
    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        if text[i] != pattern[j]:
            i -= j  # 다음 시작점 찾기
            j = -1  # 틀렸을 때 j는 항상 0 이됨
        i += 1
        j += 1  # 맞았을때 j와 i는 +1
    if j == len(pattern):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
'''

'''
있나 없나 확인만 하니까 간단하게 가능
T = int(input())
for tc in range(1,T+1):
    pattern = input()  # j
    text = input()  # i

    if pattern in text:
        print('1')
    else:
        print('0')
'''

''' 김현규님 답 
T = int(input())
 
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    len1 = len(str1)
    len2 = len(str2)
 
    is_same = False                     # 같은 문자열이 있다면 True
    for i in range(len2-len1+1):      # 고지식한 방법으로 순회
        if str2[i:i+len1] == str1:
            is_same = True
            break
 
    print(f'#{tc} {int(is_same)}')
'''








