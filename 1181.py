n = int(input())
s = set()

for i in range(n):
    word = input()
    s.add((word,len(word)))

ary = list(s)
ary.sort(key = lambda x:(x[1],x[0]))

for i in range(len(ary)):
    print(ary[i][0])
