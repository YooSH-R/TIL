# 문자열 메서드 체이닝
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')
print(new_text)  # HEzzO, WOrLD!


# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1)  # HEllO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 한 줄로 실행하기 (위와 동일한 결과)
new_text = text.swapcase().replace('l', 'z')
print('최종 결과:', new_text)  # HEzzO, WOrLD!


# 리스트 메서드 체이닝

# 1. 리스트 메서드 체이닝의 흔한 실수
numbers = [3, 1, 4, 1, 5, 9, 2]

# [실수 1] sort()는 None을 반환하므로, 변수에 아무것도 저장되지 않음
result = numbers.copy().sort()
print(result)  # None (정렬된 리스트를 기대했으나 None 출력)

# [실수 2] append()가 반환한 None 뒤에 메서드를 이을 수 없음
numbers.append(7).extend(
    [8, 9]
)  # AttributeError: 'NoneType' object has no attribute 'extend'


# 2. 올바른 해결책 (Good Cases)
numbers = [3, 1, 4, 1, 5, 9, 2]

# [해결 1] 내장 함수 sorted() 사용 (추천)
# sorted()는 정렬된 '새로운 리스트'를 반환하므로 변수에 할당 가능
# (원본을 건드리지 않으므로 copy()를 굳이 쓸 필요 없음)
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]

# [해결 2] 메서드를 단계별로 나누어 작성
# 체이닝을 포기하고, 명확하게 한 줄씩 실행
copied_list = numbers.copy()
copied_list.sort()
print(copied_list)  # [1, 1, 2, 3, 4, 5, 9]
