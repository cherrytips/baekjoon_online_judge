import sys
readline = sys.stdin.readline

word = readline().strip()
s = 0
e = len(word)-1
res = 1

while s <= e:
    if word[s] != word[e]:
        res = 0
        break
    s += 1
    e -= 1

print(res)
