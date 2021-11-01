# 1. Pass function to argument (인자로 사용될 함수)
def my_func(func): 
    return func

def my_argument_func():
    return 'Hello My func!'

result = my_func(my_argument_func) # 콜백함수로 my_argument_func가 들어가있다. 
print(result())


# 2. map
numbers = [0, 9, 99]

def plus_one(number):  # numbers의 요소에 1씩 더한 새로운 리스트 작성 
    return number + 1

print(list(map(plus_one, numbers))) 
numbers2 = list(map(plus_one, numbers))

print(numbers)
print(numbers2)