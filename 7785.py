n = int(input())

name_dic = {}

for _ in range(n):
    name,enter = map(str,input().split())

    if enter == "leave":
        del name_dic[name]
    else:
        name_dic[name] = enter

name_dic = dict(sorted(name_dic.items(),key=lambda x: x[0],reverse=True))

for i in name_dic.keys():
    print(i)
