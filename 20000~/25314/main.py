import sys
readline = sys.stdin.readline

N = int(readline())
ans = ''

for _ in range(0, N, 4):
    ans = 'long ' + ans

print(ans + 'int')
