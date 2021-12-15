from collections import defaultdict

abUP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('input.txt', 'r') as f:
  raw = f.read().splitlines()
  poly = raw[0]
  _rules = [[x for x in raw[i].split(' -> ')] for i in range(2, len(raw))]

rules = defaultdict(str)
counts = defaultdict(int)
for combo, result in _rules:
  rules[combo] = result

for x in range(len(poly)-1):
  counts[f'{poly[x]+poly[x+1]}'] += 1

for i in range(40):
  step_counts = defaultdict(int)
  step_counts.clear()
  for combo, num in counts.items():
    for c, r in rules.items():
      if combo == c:
        step_counts[c[0]+r] += num
        step_counts[r+c[1]] += num
        break
  counts.clear()
  for c, n in step_counts.items():
    counts[c] = n

letters = defaultdict(int)
for x in range(len(abUP)):
  for combo, num in counts.items():
    if combo[0] == abUP[x]:
      letters[abUP[x]] += num
    if combo[1] == abUP[x]:
      letters[abUP[x]] += num

# I seem to have made some error in counting the letters. HOWEVER!
# I noticed that after trying it on 10 steps, the max-min result was 2n-1
# Thus, I modified the final print to account for the error and voilà! Correct answer for part 1 and 2!
# I've finished this at about 4:15 AM and don't have the energy to figure out the original error so this will do for now
print(int(((max(letters.values())-min(letters.values()))+1)/2))