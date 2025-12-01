n,k = map(int,input().split())
x = 1
y = 1


if n == 0 or k==0:
    print(1)
else:
    for i in range(k):
        x = n * x
        n -= 1

        y = k * y
        k -= 1
    print(x//y)



