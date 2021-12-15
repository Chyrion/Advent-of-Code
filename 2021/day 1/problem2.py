raw = [int(x) for x in (open('input.txt', 'r').read().splitlines())]
inc = 0
for i in range(len(raw)-3):
  if sum(raw[i+1:i+4]) > sum(raw[i:i+3]):
    inc += 1
print(inc)