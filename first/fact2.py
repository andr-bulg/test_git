def fact2(n):
  fact = 1
  for i in range(2, n + 1):
    fact *= n
  return fact

if __name__ == '__main__':
  print(fact2(5))
