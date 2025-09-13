h,m = map(int,input().split())
cook = int(input())

ans_h, ans_m = divmod(60*h+m+cook,60)

print(ans_h%24,ans_m)

