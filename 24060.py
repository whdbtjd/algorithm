a,k = map(int,input().split())

cnt = 0

def merge_sort(a,p,r):
    global k
    global cnt
    if p < r:
        q = (p + r) // 2
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)


def merge(a,p,q,r):
    i = p
    j = q + 1
    t = 0
    tmp = [0] * (r - p + 1)
    while i <= q and j <= r:

        if a[i] <= a[j]:
            tmp[t] = a[i]
            t += 1
            i += 1
        else:
            tmp[t] = a[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = a[i]

        t += 1
        i += 1
    while j <= r:
        tmp[t] = a[j]

        t += 1
        j += 1
    i = p
    t = 0

    global cnt
    global k

    while i <= r:
        cnt += 1
        a[i] = tmp[t]
        if cnt == k:
            print(tmp[t])
        i += 1
        t += 1









ary = list(map(int,input().split()))
merge_sort(ary,0,len(ary)-1)

if cnt < k:
    print(-1)




