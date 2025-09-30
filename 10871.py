n,x = map(int,input().split())

a = map(int,input().split())

print(" ".join(map(int,filter(lambda i: i < x, a))))


