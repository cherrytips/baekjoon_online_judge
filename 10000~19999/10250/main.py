T = int(input())
for i in range(T):
  H, W, N = map(int, input().split())
  floor = N % H if N % H != 0 else H
  room = int(N/H)+1 if N % H != 0 else int(N/H)
  if room < 10:
    print(f'{floor}0{room}')
  else:
    print(f'{floor}{room}')
