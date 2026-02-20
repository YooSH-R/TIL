class Singer:
    pass

iu = Singer()
bts = Singer()

# iu와 bts는 Singer 클래스의 인스턴스
print(type(iu))  # <class '__main__.Singer'>
print(type(bts))


# 문자열 변수 name은 (정확히는 'Alice')는 str 클래스의 인스턴스
name = 'Alice'
print(type(name))  # <class 'str'>

data = [1, 2, 3]
print(type(data))  # <class 'list'>

# 데이터들이 메서드를 호출할수 있었던 이유
# 문자열 name이 사용할 수 있는 메서드인 split()은 클래스 str에 정의되어 있음
# 리스트 data가 사용할 수 있는 메서드인 append()는 클래스 list에 정의되어 있음