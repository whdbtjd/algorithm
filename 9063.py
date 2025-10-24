n = int(input())
x_ary = []
y_ary = []

for i in range(n):
   x,y = map(int,input().split())

   x_ary.append(x)
   y_ary.append(y)

if n > 1:
    print((max(x_ary)-min(x_ary)) * (max(y_ary) - min(y_ary)))
else:
    print(0)

