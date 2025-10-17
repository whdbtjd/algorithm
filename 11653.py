n = int(input())


for i in range(2,int(n**0.5)+1):
     while True:
        if n % i == 0:
            print(i)
            n = n // i
        if n % i != 0:
            break
if n != 1:
   print(n)



