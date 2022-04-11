a, b, c = map(int, input().split())

if a == b:
    if b == c:
        print(f'{10000+a*1000}')
    else:
        print(f'{1000+a*100}')
elif a == c or b == c:
    print(f'{1000+c*100}')
else:
    l = [a, b, c]
    l.sort()
    print(f'{l[len(l)-1]*100}')
