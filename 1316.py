n = int(input())
ans = 0

for i in range(n):
    word = input()
    cnt = set()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            if word[j+1] in cnt:
                cnt.clear()
                break
            cnt.add(word[j])

    if len(set(word)) - 1 == len(cnt) or len(set(word)) == 1:
        ans += 1

print(ans)









