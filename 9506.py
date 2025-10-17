while True:
    n = int(input())
    if n == -1:
        break

    ans = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            ans.update([i, n // i])

    if sum(ans) == n:
        ans = sorted(ans)
        print(f"{n} = {' + '.join(map(str, ans))}")
    else:
        print(f"{n} is NOT perfect.")
