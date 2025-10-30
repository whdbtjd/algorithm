n,k = map(int,input().split())

score = [int(x) for x in input().split()]
score.sort()

print(score[n-k])
