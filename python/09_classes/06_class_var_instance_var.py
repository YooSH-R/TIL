class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


# 인스턴스 생성
c1 = Circle(5)
c2 = Circle(10)

# 인스턴스 변수(속성) 접근
print(c1.radius)  # 5
print(c2.radius)  # 10

# 인스턴스 c1의 인스턴스 변수 pi를 생성
c1.pi = 100

# 인스턴스 c1의 인스턴스 변수 pi를 출력
print(c1.pi)  # 100

# 클래스 변수 접근
print(Circle.pi)  # 3.14

# 반면 인스턴스 c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi)  # 3.14
