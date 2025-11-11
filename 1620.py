n,m = map(int,input().split())

ary = {}

for i in range(n):
    name = input()
    ary[name] = i + 1

ary_list = list(ary)

for i in range(m):
    test = input()

    if test.isdigit():
        idx = int(test)
        print(ary_list[idx - 1])
    else:
        print(ary[test])

