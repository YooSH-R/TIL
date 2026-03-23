import numpy as np


"""
기본 행렬 생성 및 연산
"""

print([1, 2, 3, 4, 5])
# numpy의 ndarray를 만드는 함수
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

a = np.array([
    [1, 2], 
    [3, 4],
])
b = np.array([
    [4, 3],
    [2, 1],
])
print(a)
print(b)
# @: 행렬 곱 연산
print(a @ b)
"""
[[ 8  5]
 [20 13]]
"""

# 단위 행렬: 정사각행렬의 1
E = np.eye(2)
print(E)
print(a @ E)  # a
print(b @ E)  # b

print(np.eye(4))


# 행렬의 원소를 인덱스를 바탕으로 변경하기
x = np.eye(3)
x[0, 2] = 47
x[2, 0] = 9
print(x)

"""
무작위 정수 만들기
"""
arr_ran = np.random.randint(low=50, high=101, size=(5))
print(arr_ran)
arr_ran = np.random.randint(low=50, high=101, size=(2, 2))
print(arr_ran)

# 정규분포 추출
std_ran = np.random.randn(2, 4)
print(std_ran)



"""
연산 / 형변환
"""
id_3 = np.eye(3)
std_ran = np.random.randn(3, 3)
# 다양한 차원에 대한 곱 / 내적
z = np.dot(id_3, std_ran)
print(std_ran)
print(z)

# 각 원소의 형변환
id_bool = id_3.astype(bool)
print(id_bool)
id_int = id_3.astype(int)
print(id_int)

# 상수 곱 (스칼라 배)
x_float = id_3 * 1.1
print(x_float)


"""
백터 연습
"""
v = np.array([1, 2, 3])
print(v)

v_repeated = np.tile(v, (3, 1))
print(v_repeated)

v_flattened = v_repeated.flatten()
print(v_flattened)

# 균등한 간격을 가지는 일정 크기의 벡터 생성
thetas = np.linspace(0, 2 * np.pi, 120)
print(thetas)
print(np.sin(thetas))
