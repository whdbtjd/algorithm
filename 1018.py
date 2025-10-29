n,m = map(int,input().split())
ary = []

for i in range(n):
    ary.append(input())

wb_ary = [[0] * 8 for i in range(8)]
bw_ary = [[0] * 8 for i in range(8)]

wb_ans = []
bw_ans = []

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            wb_ary[i][j] = "W"
            bw_ary[i][j] = "B"
        else:
            wb_ary[i][j] = "B"
            bw_ary[i][j] = "W"

for i in range(n-7):
    for j in range(m-7):
        wb_cnt = 0
        bw_cnt = 0
        for x in range(8):
            for y in range(8):
                if ary[i + x][j + y] != wb_ary[x][y]:
                    wb_cnt +=1

                if ary[i + x][j + y] != bw_ary[x][y]:
                    bw_cnt +=1
        wb_ans.append(wb_cnt)
        bw_ans.append(bw_cnt)

print(min(min(wb_ans),min(bw_ans)))
