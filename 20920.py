import sys
input = sys.stdin.readline
n,m = map(int,input().split())

word = {}

for _ in range(n):
    book = input().rstrip()

    if len(book) >= m:
        word[book] = word.get(book,0) + 1

ans = sorted(word.items(), key = lambda x:(-x[1],-len(x[0]),x[0]))

for i,j in ans:
    print(i)
