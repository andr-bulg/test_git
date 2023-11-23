def fact2(n):
  fact = 1
  for i in range(2, n ):
    fact *= i
  return fact

if __name__ == '__main__':
  print(fact2(0))
  print(fact2(5))

