ary = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
word = input()
ans = 0


for i in word:
    for j in ary:
        if i in j:
            ans += ary.index(j)+3

print(ans)






