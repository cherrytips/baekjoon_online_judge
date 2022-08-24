def Rev(x):
  return ''.join(list(reversed(x)))


X, Y = input().split()
print(int(Rev(str(int(Rev(X))+int(Rev(Y))))))
