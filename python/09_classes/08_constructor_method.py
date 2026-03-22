class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.
Person.greeting(person1)  # 안녕하세요. 지민입니다.
print(person1.name)  # 지민
