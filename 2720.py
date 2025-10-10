t = int(input())
ans = [0,0,0,0]

for i in range(t):
    price = int(input())
    print(price//25, price%25//10, price%25%10//5, price%25%10%5)
