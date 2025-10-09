ans = [[""] * 5 for _ in range(15)]

for i in range(5):
    word = input()
    for j in range(len(word)):
      ans[j][i] = word[j]

for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] != "":
            print(ans[i][j],end="")


