import sys
readline = sys.stdin.readline

T = int(readline().strip())

for _ in range(T):
    S = readline().strip()
    res = ''
    res += S[0]
    res += S[-1]
    print(res)
