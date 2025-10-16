x = int(input())
idx = 1
total = 1

while True:
    if total > x:
        idx -= 1
        break
    else:
        total += idx
        idx += 1

line_idx = x % (total - idx) + 1

tlqkf = idx + 1

if idx % 2 != 0 :
  print(f"{tlqkf - line_idx}/{line_idx}")
else:
  print(f"{line_idx}/{tlqkf -line_idx}")



