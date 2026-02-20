# 기존: 기본 딕셔너리
text = 'banana'
counts = {}

for char in text:
    if char not in counts:  # 키가 있는지 매번 확인해야 함
        counts[char] = 0
    counts[char] += 1

print(counts)  # {'b': 3, 'a': 3, 'n': 2}


# 개선: defaultdict 활용
from collections import defaultdict

text = 'banana'
counts = defaultdict(int)  # 기본값을 정수(0)로 설정

for char in text:
    # 키 확인 불필요! 없으면 0으로 자동 생성 후 +1
    counts[char] += 1

print(counts)  # defaultdict(<class 'int'>, {'b': 1, 'a': 3, 'n': 2})


# 활용 예제
# 색상별 과일 분류
fruits = [('red', 'apple'), ('yellow', 'banana'), ('red', 'cherry')]
fruit_by_color = defaultdict(list)

for color, fruit in fruits:
    # color 키가 없으면 빈 리스트 생성 -> append 바로 가능
    # print(fruit_by_color)
    fruit_by_color[color].append(fruit)

print(
    fruit_by_color
)  # defaultdict(<class 'list'>, {'red': ['apple', 'cherry'], 'yellow': ['banana']})
print(
    dict(fruit_by_color)
)  # {'red': ['apple', 'cherry'], 'yellow': ['banana']}
