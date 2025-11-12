s = input()

word = set()
word_len = 1

while True:
    for i in range(len(s) - word_len + 1):
        word.add(s[i: i + word_len])

    if word_len == len(s):
        break

    word_len += 1

print(len(word))
