N = int(input())
t = list(map(int, input().split()))
answer = 0

t.sort(reverse=True)

for i in range(N):
  t[i] -= (N-i)
  if t[i] < 0:
    t[i] = 0
  answer += 1

t.sort()

print(t[len(t)-1]+N+2)
