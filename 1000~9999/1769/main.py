X = input()
Y = X
count = 0

while len(Y) > 1:
  Y = str(sum(list(map(int, list(Y)))))
  count += 1

print(count)

if int(Y) % 3 == 0:
  print('YES')
else:
  print('NO')
