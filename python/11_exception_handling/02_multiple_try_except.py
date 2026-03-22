# 복수 예외처리
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 입력해주세요.')


try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
pass
