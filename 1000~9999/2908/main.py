A, B = input().split()


def reverse_str_return(list):
  result = ''
  list.reverse()
  for i in range(len(list)):
    result += list[i]
  return result


for i in reversed(range(len(A))):
  if A[i] != B[i]:
    if int(A[i]) > int(B[i]):
      print(reverse_str_return(list(A)))
      break
    else:
      print(reverse_str_return(list(B)))
      break
