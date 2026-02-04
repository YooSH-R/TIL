## 시간 문제에서는 시, 분을 하나로 합친 후 //,  % 써보기

## 중복 문제에서는 set 사용 고려해보기

## iterable객체의 요소들을 순회하여 각각을 모두 더하기
- 빈 객체 만들어서 += 하면 되지

## input에서 공백검사하고싶을때
- strip() 메서드 사용

## 브루트포스(Brute Force) 알고리즘
- 가능한 모든 경우를 전부 시도해서 정답을 찾는 알고리즘

## Combination
- n개 중에 3개 뽑는 모든 경우의 수
```py
for i in range(n - 2):
  for j in range(i + 1, n - 1):
    for k in range(j + 1, n):
```

## map 함수
- map함수는 한번만 소비된다 -> max(map())한번 쓰면 min(map())불가능

# for문
- for 문의 iterable의 파라미터가 증가되는 형식의 for문
```py
for _ in range(a):
  a += 1
```
- 무한정으로 돌아가 Error?
- a는 for문 시작할 때 한번만 평가