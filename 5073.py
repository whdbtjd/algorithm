while True:
    sides = list(map(int, input().split()))
    if sides == [0, 0, 0]:
        break

    sides.sort()
    a, b, c = sides

    if a + b <= c:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
