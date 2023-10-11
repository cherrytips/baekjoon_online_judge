import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
bucket = [[] for _ in range(N+1)]
res = ''

for m in range(M):
    i, j, k = map(int, readline().split())
    for n in range(i, j+1):
        if bucket[n]:
            bucket[n].clear()
        bucket[n].append(k)

for b in bucket[1:]:
    if b:
        res += (str(b[0]) + ' ')
    else:
        res += (str('0') + ' ')

print(res)
