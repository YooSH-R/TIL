# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']
"""
실행 결과
{'A': 4, 'B': 3, 'O': 3, 'AB': 2}
"""


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    blood_count_bracket = {}
    for blood in blood_types:
        if blood in blood_count_bracket:
            blood_count_bracket[blood] += 1
        else:
            blood_count_bracket[blood] = 1
    return blood_count_bracket


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    blood_count_bracket = {}

    for blood in blood_types:
        blood_count_bracket[blood] = blood_count_bracket.get(blood, 0) + 1

    return blood_count_bracket


# 3. defaultdict를 사용한 방법
# (키가 없을 때 자동으로 0으로 초기화해주므로 로직이 단순해짐)
from collections import defaultdict


def count_blood_types(blood_types):
    # int() 함수는 실행 시 0을 반환하므로, 기본값을 0으로 설정하는 효과
    blood_count = defaultdict(int)

    for blood in blood_types:
        blood_count[blood] += 1

    return dict(blood_count)  # 일반 딕셔너리로 변환하여 반환


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
