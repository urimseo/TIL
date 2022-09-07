'''
num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환
'''

def solution(num):
    answer = 'Even'
    if num % 2:
        answer = 'Odd'
    return answer