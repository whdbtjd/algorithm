import sys


def blank(ary,start,end):
    if end != start:
        remove_start = start + (end - start + 1) // 3
        remove_end = remove_start + (end - start + 1) // 3 - 1
        for i in range(remove_start,remove_end + 1):
            ary[i] = " "
        blank(ary,start,remove_start - 1)
        blank(ary,remove_end + 1,end)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    ary = ["-"] * 3 **n
    blank(ary,0,len(ary) - 1)
    print("".join(ary))




