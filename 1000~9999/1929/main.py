import math

M, N = map(int, input().split())


def find_decimal(number):
  sq = int(math.sqrt(num))

  for i in range(2, sq+1):
    if number % i == 0:
      return False

  return True


for num in range(M, N+1):
  if num != 1 and find_decimal(num):
    print(num)
