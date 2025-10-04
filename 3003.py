n = list(map(int,input().split()))
ary = [1,1,2,2,2,8]
ans = [0] * 6


for i in range(len(n)):
    ans[i] = ary[i] - n[i]
    print(ans[i],end=" ")

