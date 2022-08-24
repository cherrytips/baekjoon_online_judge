N = int(input())


def func(N):
  for num in range(N):
    temp = num + sum(map(int, list(str(num))))
    if temp == N:
      return num

  return 0


print(func(N))
