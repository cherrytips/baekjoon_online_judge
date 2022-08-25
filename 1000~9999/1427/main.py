N = list(map(int, input()))
result = 0
index = 0

N.sort(reverse=True)

for i in reversed(range(len(N))):
  result += (N[index]*(10**i))
  index += 1

print(result)