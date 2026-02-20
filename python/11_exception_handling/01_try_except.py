# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

try:
    num = int(input('숫자를 입력해주세요: '))
except ValueError:
    print('그건 숫자가 아닙니다....')