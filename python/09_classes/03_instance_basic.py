class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')


p1 = Person('Alice', 25)
p1.introduce()  # "안녕하세요. 저는 Alice, 나이는 25살입니다."

p2 = Person('Bella', 30)
p2.introduce()  # "안녕하세요. 저는 Bella, 나이는 30살입니다."
