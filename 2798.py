import bisect

n,m = map(int,input().split())
ary = []
total_sum = set()

ary = list(map(int,input().split()))

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            num = ary[i] + ary[j] + ary[k]
            total_sum.add(num)

total_sum = list(total_sum)
total_sum.sort()

ans = bisect.bisect_right(total_sum,m) - 1
print(total_sum[ans])

