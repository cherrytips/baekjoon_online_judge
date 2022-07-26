import sys
input = sys.stdin.readline

N = int(input())
asm = []
answer = 0

for i in range(N):
  x = input()

  if x[0] == '1':
    ox, A, T = x.split()
    asm.append([int(A), int(T)-1])
  else:
    if len(asm) == 0:
      continue
    asm[-1][1] -= 1

  if asm[-1][1] == 0:
    answer += asm[-1][0]
    asm.pop()

print(answer)
