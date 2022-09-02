def solution(array, commands):
    answer = []
    for com in commands:
        arr = array[com[0]-1:com[1]] # 배열 슬라이싱 
        arr.sort() # 정렬
        answer.append(arr[com[2]-1]) # 해당하는 수 뽑아서 담기

    return answer

    # 람다식 사용하여 풀이하는 방법
    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
#	[5, 6, 3]

