n = int(input())
ary = []

for i in range(n):
    age, name = input().split()
    ary.append((int(age), i, name))

ary.sort(key=lambda x: (x[0], x[1]))

for a, _, n in ary:
    print(a, n)
