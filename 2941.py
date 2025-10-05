word = input()
alpa = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in alpa:
    word = word.replace(i," ")

print(len(word))
