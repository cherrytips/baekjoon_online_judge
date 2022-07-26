import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0

A.sort()
B.sort(reverse=True)

for n in range(N):
  answer += A[n]*B[n]

print(answer)
