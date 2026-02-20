class Counter:
    def __init__(self):
        self.count = 0

    # 인스턴스 메서드
    def increment(self):
        # 이 메서드를 호출하는 인스턴스의 변수 count를 1 증가 시키는 메서드
        self.count += 1

c1 = Counter()
c2 = Counter()
# 인스턴스 메서드 호출
print(c1.count)  # 0
c1.increment()
print(c1.count)  # 1
print(c2.count)  # 0
