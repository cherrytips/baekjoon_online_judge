import sys
readline = sys.stdin.readline

N = int(readline().strip())
star = 1
space = N-1

for _ in range(N):
    temp = ' '*space
    temp += '*'*star
    print(temp)
    star += 2
    space -= 1

star -= 4

for i in range(1, N):
    temp = ' '*i
    temp += '*'*star
    print(temp)
    star -= 2
