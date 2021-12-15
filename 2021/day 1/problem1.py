raw = [int(x) for x in (open('input.txt', 'r').read().splitlines())]

inc = 0
for i in range(1, len(raw)):
  if raw[i] > raw[i-1]:
    inc += 1

print(inc)