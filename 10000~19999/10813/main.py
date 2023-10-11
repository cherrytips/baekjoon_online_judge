import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
bucket = []
res = ''

for n in range(N+1):
    bucket.append(n)

for _ in range(M):
    i, j = map(int, readline().split())
    temp = bucket[i]
    bucket[i] = bucket[j]
    bucket[j] = temp

for b in bucket[1:]:
    res += (str(b) + ' ')

print(res)
