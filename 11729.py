n = int(input())

def circle(n, start, end, middle):
    if n == 0:
        return

    circle(n-1, start, middle, end)
    print(start, end)
    circle(n-1, middle, end, start)

circle(n, 1, 3, 2)
