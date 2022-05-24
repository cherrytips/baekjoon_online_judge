N = int(input())
scores = input().split(' ')

for i in range(N):
    scores[i] = int(scores[i])

scores.sort()
M = scores[len(scores)-1]

average = 0
for i in range(N):
    average += (scores[i]/M*100)

print(average/N)
