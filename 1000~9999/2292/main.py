N = int(input())
cnt = 1
prev = 0
next = 1
result = 0

while N >= prev:
  result += 1
  next += cnt*6
  prev = next - cnt*6 + 1
  cnt += 1

print(result)

'''
1
1+1 1+6
1+1+6 1+6+12
1+1+6+12 1+6+12+18
1+1+6+12+18 1+6+12+18+24
'''
