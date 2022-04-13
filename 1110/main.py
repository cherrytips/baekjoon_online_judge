N = input()
origin = N
cnt = 0

while True:
    if int(N) < 10:
        N = '0'+str(int(N))
    ls = str(int(N[0])+int(N[1]))
    N = N[1] + ls[len(ls)-1]
    cnt += 1
    if int(N) == int(origin):
        break

print(cnt)
