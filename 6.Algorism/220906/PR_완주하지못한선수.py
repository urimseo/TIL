# 각 리스트를 정렬하여 비교
def solution(participant, completion):
  participant.sort()
  completion.sort()

  for i in range(len(completion)):
    if completion[i] != participant[i]:
      return participant[i]
  # 만일 비교해도 나오지 않는다면 맨 마지막 선수가 완주하지 못한 것
  return participant[-1]

# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# Counter 을 사용하여 풀이 

import collections

def solution_1(par, com):
    print(collections.Counter(par)) # Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
    print(collections.Counter(com)) # Counter({'stanko': 1, 'ana': 1, 'mislav': 1})

    # 카운터 객체는 값을 뺄 수 있다!!!
    answer = collections.Counter(par) - collections.Counter(com) 
    print(answer) # Counter({'mislav': 1}) 

    return list(answer.keys())[0]

print(solution_1(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))



# 반복문을 이용한 풀이 -> remove를 이용해서인지 효율성에서 fail
def solution2(participant, completion):
    answer = ''
    copy = participant[:]

    for k in participant:
      if k in completion:
        copy.remove(k)
        completion.remove(k)
    answer = copy[0]
    return answer

def solution3(participant, completion):
    answer = ''
    copy = participant[:]

    for k in participant:
      if k not in completion:
        answer = k
        break
      else:
        copy.remove(k)
        completion.remove(k)
    return answer

def solution4(participant, completion):
    answer = ''

    for k in completion:
        participant.remove(k)
    answer = participant[0]
    return answer



