import sys

N = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
all = list(map(int, sys.stdin.readline().split()))

have.sort()


def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start+end)//2

    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid-1
    else:
      start = mid+1
  return None


for i in range(M):
  if binary_search(have, all[i], 0, N-1) != None:
    print(1, end=' ')
  else:
    print(0, end=' ')
