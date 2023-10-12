import sys
readline = sys.stdin.readline

N = int(readline().strip())
board = [[0 for _ in range(100)] for _ in range(100)]
res = 0

for _ in range(N):
    s, e = map(int, readline().split())

    for i in range(e, e+10):
        for j in range(s, s+10):
            board[i][j] = 1

for b in board:
    res += b.count(1)

print(res)
