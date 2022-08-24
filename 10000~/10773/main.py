import sys
input = sys.stdin.readline

K = int(input())
table = []

for k in range(K):
  num = int(input())

  if num == 0:
    table.pop()
  else:
    table.append(num)

print(sum(table))
