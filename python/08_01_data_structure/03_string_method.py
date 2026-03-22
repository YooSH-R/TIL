################ 문자열 탐색 및 검증 ################

# find
text = 'banana'
print(text.find('a'))  # 1
print(text.find('z'))  # -1

# isupper
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False

# islower
print(string1.islower())  # False
print(string2.islower())  # False

# isalpha
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False


################ 문자열 조작 ################

# replace
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world

# strip
# 사용자 입력 등에서 불필요한 공백이 포함된 경우
text = '   Hello    World   '

# 1. 아무것도 지정하지 않으면 '공백(띄어쓰기, 탭, 엔터)'을 제거
clean_text = text.strip()

print(clean_text)
# 결과: 'Hello    World'
# (주의: 문자열 중간의 공백은 제거되지 않음)


# 2. 제거할 문자를 지정하는 경우
text = '!!!Hello World!!!'
print(text.strip('!'))
# 결과: 'Hello World'


# [심화] 문자열 집합으로 제거 (순서 상관 없음)
# 'w', '.', 'c', 'o', 'm' 중 하나라도 양쪽 끝에 있으면 계속 제거
url = 'www.example.com'
print(url.strip('w.com'))
# 결과: 'example'
# (왼쪽의 'www.'과 오른쪽의 '.com'이 모두 제거됨)


# split
# 1. 공백을 기준으로 분리 (기본 동작)
# - 여러 개의 공백도 하나로 처리하며, 앞뒤 공백은 무시함
text = '  Hello    Python  '
print(text.split())
# 결과: ['Hello', 'Python’]


# 2. 특정 문자를 기준으로 분리
# - 지정한 문자를 기준으로 '엄격하게' 분리함 (빈 문자열 발생 가능)
data = '10,20,,30'
print(data.split(','))
# 결과: ['10', '20', '', '30']


# 3. 분할 횟수 제한 (maxsplit)
# - 앞에서부터 1번만 자르고 나머지는 그대로 둠
path = 'User/admin/documents'
print(path.split('/', maxsplit=1))
# 결과: ['User', 'admin/documents']


# join
words = ['Python', 'is', 'awesome']

sentence1 = ' '.join(words)
sentence2 = '-'.join(words)

print(sentence1)  # Python is awesome
print(sentence2)  # Python-is-awesome


# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!
