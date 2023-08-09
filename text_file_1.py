# 프로젝트 1: 전화번호 가려주는 프로그램

numbers = '010-12345-23456'

def change_num(nums):
    answer = nums.replace(nums[-5:], '#####')
    return answer

print(change_num(numbers))

# 프로젝트 2: 리스트 평탄화

overlap = [[1, 2], 3, [[4, 5, 6], 7], 8, 9]

def flatten(data):
    output = []

    for y in data:
        if type(y) == list:
            output += flatten(y)
        else:
            output.append(y)
    return output

print(flatten(overlap))

# 프로젝트 3: 10 이하 숫자만 곱해주는 함수

def multiplier(*values):
    output = 1
    
    for n in values:
        if n <= 10:
            output *= n
        else: pass
    
    return output

print(multiplier(2, 3, 4, 5))
print(multiplier(3, 12, 10))
