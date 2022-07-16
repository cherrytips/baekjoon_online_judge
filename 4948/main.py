import math


def find_decimal(number):
  sq = int(math.sqrt(number))

  for i in range(2, sq+1):
    if number % i == 0:
      return False

  return True


while True:
  n = int(input())
  cnt = 0

  if n == 0:
    break

  for num in range(n+1, 2*n+1):
    if num != 1 and find_decimal(num):
      cnt += 1

  print(cnt)
