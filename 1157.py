word = input()
ary = word.upper()
word = set(ary)

max = 0
ans = 0

for i in word:
    if max == ary.count(i):
        ans = "?"
    elif ary.count(i) > max:
        max = ary.count(i)
        ans = i

print(ans)


