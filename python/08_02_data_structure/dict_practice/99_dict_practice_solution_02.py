# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기


# 1. [] 표기법을 사용한 방법
def dict_invert(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        # 딕셔너리 안에 없는 경우 -> key-value 값 생성
        if value not in new_dict:
            new_dict[value] = [key]
        # 딕셔너리 안에 있는 경우 -> value 리스트에 요소 하나 추가
        else:
            new_dict[value].append(key)
    return new_dict


# 2. get 메서드를 사용한 방법
def dict_invert(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[value] = new_dict.get(value, []) + [key]
    return new_dict


# 3. defaultdict를 사용한 방법
from collections import defaultdict


def dict_invert(input_dict):
    # 키가 없을 때 자동으로 빈 리스트([])를 생성하도록 설정
    new_dict = defaultdict(list)

    for key, value in input_dict.items():
        # new_dict[value]가 없으면 자동으로 []가 생성되므로 바로 append 가능
        new_dict[value].append(key)

    return dict(new_dict)  # 일반 딕셔너리 형태로 반환 (선택 사항)


# 테스트 코드
print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
print(
    dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
)  # {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}
