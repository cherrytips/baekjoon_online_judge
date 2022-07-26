import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
result = 0

for n in range(N):
  coin = int(input())
  if coin > K:
    continue
  coins.append(coin)

index = len(coins)-1

while K > 0:
  result += int(K/coins[index])
  K %= coins[index]
  index -= 1

print(result)
