n = int(input())
cnt = n - 1

while cnt > 0:
    n = n * cnt
    cnt -= 1

if n == 0:
   print(1)
else:
    print(n)
