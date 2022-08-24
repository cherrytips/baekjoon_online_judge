from math import sqrt


def is_decimal(num):
  for i in range(2, int(sqrt(num))+1):
    if num % i == 0:
      return False
  return True


T = int(input())

for i in range(T):
  num = int(input())
  par_1 = num//2
  par_2 = num-par_1

  while True:
    if is_decimal(par_1) and is_decimal(par_2):
      print(par_1, par_2)
      break
    else:
      par_1 -= 1
      par_2 += 1
