N = int(input())
nums = []

for _ in range(N):
  nums.append(int(input()))

nums.sort()

m = nums[0]

for i in range(2, m+1):
  rest = set()
  
  for j in range(N):
    rest.add(nums[j] % i)

  if len(rest) == 1:
    print(i, end=' ')
