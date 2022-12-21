input = [x for x in (open('input.txt', 'r').read().splitlines())]
rows = []
for row in input:
  new_row = []
  for n in [*row]:
    new_row.append(int(n))
  rows.append(new_row)

scores = []


for row in rows:
  for num in row:
    

print(max(scores))

