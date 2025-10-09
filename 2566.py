ary = [[0] * 9 for _ in range(9)]
max_value = 0
n,m = 0,0

for i in range(9):
   ary[i] = list(map(int,input().split()))
   row_max = max(ary[i])
   if row_max > max_value:
     max_value = row_max
     n,m = i,ary[i].index(max_value)

print(max_value)
print(n+1, m+1)
