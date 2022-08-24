result = []
piece = list(map(int, input().split()))
normal = [1, 1, 2, 2, 2, 8]

for i in range(len(piece)):
  print(normal[i]-piece[i])