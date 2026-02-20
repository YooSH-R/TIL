# 리스트를 생성하는 방법 비교

# 1. loop
result1 = []
for i in range(10):
    result1.append(i)

# 2. list comprehension
result2 = [i for i in range(10)]
# result2 = list(i for i in range(10))

# 3. map
result3 = list(map(lambda i: i, range(10)))

print(result1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(result2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(result3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
