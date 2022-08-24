import sys
input = sys.stdin.readline

N = int(input())
point = []

for i in range(N):
  x, y = map(int, input().split())
  point.append([x, y])

point.sort()

for p in point:
  print(p[0], p[1])
