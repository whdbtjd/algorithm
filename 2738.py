n,m = map(int,input().split())
A = [m * [0] for _ in range(n)]
B = [m * [0] for _ in range(n)]
total = [m * [0] for _ in range(n)]

for i in range(n * 2):
    M = list(map(int,input().split()))
    if i < n:
      A[i] = M
    else:
      B[i - n] = M

for i in range(n):
    for j in range(m):
      total[i][j] = A[i][j] + B[i][j]
      print(total[i][j],end=" ")
    print()





