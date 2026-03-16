class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        # 클래스 메서드를 통해 인스턴스가 생성될 때마다 인구 수 증가
        Person.increase_population()

    # 클래스 메서드
    @classmethod
    def increase_population(cls):
        cls.population += 1


# 인스턴스 생성
person1 = Person('Alice')
person2 = Person('Bob')

# 클래스 변수 접근
print(Person.population)  # 2
