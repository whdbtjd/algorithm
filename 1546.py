n = int(input())
ary = list(map(int,input().split()))

num = max(ary)

ary = [i/num*100 for i in ary]
print(sum(ary)/len(ary))
