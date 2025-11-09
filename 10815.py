n = int(input())
ary_n = set(map(int,input().split()))

m = int(input())
ary_m = list(map(int,input().split()))

for i in ary_m:
    if i in ary_n:
        print(1,end = " ")
    else:
        print(0,end = " ")


