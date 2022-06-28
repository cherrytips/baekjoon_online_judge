N = int(input())
numbers = list(map(int, input().split()))


def find_decimal(number):
  result = True
  for i in range(2, number):
    if number % i == 0:
      result = False
      break

  return result


answer = 0
for n in numbers:
  if n != 1 and find_decimal(n):
    answer += 1

print(answer)
