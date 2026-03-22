class Circle:
    pi = 3.14

    # 생성자 메서드
    def __init__(self, radius):
        self.radius = radius


# 인스턴스 생성
c1 = Circle(1)
c2 = Circle(2)


# 인스턴스 변수(속성) 접근
print(c1.radius)  # 1
print(c2.radius)  # 2

# 클래스 변수(공통 속성) 접근
print(c1.pi)
print(c2.pi)
