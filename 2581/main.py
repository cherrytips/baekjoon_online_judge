M = int(input())
N = int(input())
decimals = []
sum = 0


def find_decimal(number):
  result = True
  if number == 1:
    return False

  for i in range(2, number):
    if number % i == 0:
      result = False
      break

  return result


for i in range(M, N+1):
  if find_decimal(i):
    sum += i
    decimals.append(i)

if len(decimals) == 0:
  print(-1)
else:
  print(sum)
  print(decimals[0])
