N = int(input())
numbers = []

for n in range(N):
  numbers.append(input())

for i in range(len(numbers[0])):
  diff = set()

  for n in numbers:
    diff.add(n[-(i+1):])

  if len(diff) == N:
    print(i+1)
    break
