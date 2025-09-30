ary = []
mods= []

for i in range(10):
    ary.append(int(input())%42)

mods = set(ary)
print(len(mods))
