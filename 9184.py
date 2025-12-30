w = [[[None] *  101 for _ in range(101)] * 101 for _ in range(101)]
ans = 0

def dp(a,b,c):
     if a <= 0 or b <= 0 or c <= 0:
         return 1

     if a > 20 or b > 20 or c > 20:
         return dp(20,20,20)

     if w[a][b][c]is not None:
         return w[a][b][c]

     if a < b < c:
         w[a][b][c] = dp(a,b,c-1) + dp(a,b-1,c-1) - dp(a,b-1,c)
     else:
         w[a][b][c] = dp(a-1,b,c) + dp(a-1,b-1,c) + dp(a-1,b,c-1) - dp(a-1,b-1,c-1)

     return w[a][b][c]

while True:
    a,b,c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break
    ans = dp(a,b,c)
    print(f"w({a}, {b}, {c}) = {ans}")


