import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
A = [list(map(int, readline().split())) for _ in range(N)]
B = [list(map(int, readline().split())) for _ in range(N)]

for n in range(N):
    for m in range(M):
        print(A[n][m]+B[n][m], end=' ')
    print('')
