f = [x for x in (open('input.txt', 'r').read().splitlines())]
elves = []
a = []
for b in f:
  if b != '':
    a.append(int(b))
  elif len(a) != 0:
    elves.append(sum(a))
    a.clear()

elves.sort(reverse=True)
print(f'part 1: {elves[0]}')
print(f'part 2: {elves[0]+elves[1]+elves[2]}')