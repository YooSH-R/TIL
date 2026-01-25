def add(x, y):
  return x + y

def func():
  a = 10
  return add(a, a)
print(func())

def func2():
  b = 10
  def add2():
    return b + b
  return add2()
print(func2())