# if문 기본
score = 87

if score > 95:
    print('축하요')
else:
    print('수고요')

# else 없어도 상황에 따라서 elif까지만 사용해도 무관
if 조건1:
    "if 코드 블럭"
elif 조건2:
    "elif 코드 블럭"

# 마찬가지로 if만 써도 가능합니다.
if 조건1:
    "if 코드 블럭"




# 복수 조건문
## 순서 1. 결과: 매우 나쁨
dust = 155

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


## 순서 2. # 결과: 보통
dust = 155

if dust > 30:
    print('보통')
elif dust > 80:
    print('나쁨')
elif dust > 150:
    print('매우 나쁨')
else:
    print('좋음')


# 중첩 조건문 동작 예시
# 출력: 매우 나쁨
#      위험해요! 나가지 마세요!
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
