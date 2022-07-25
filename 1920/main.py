N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def has(num, nums):
  left = 0
  right = len(nums)-1

  while left <= right:
    mid = (left+right)//2

    if nums[mid] == num:
      return True
    elif nums[mid] < num:
      left = mid+1
    else:
      right = mid-1

  return False


A.sort()

for b in B:
  if has(b, A):
    print(1)
  else:
    print(0)
