crates, instructions = [], []
with open('input.txt','r') as f:
  file = f.read().splitlines()
  for line in file:
    if 'move' not in line and line != '':
      this_line = []
      for i in range(0,len(line),4):
        this_line.append(line[i:i+4].strip(' '))
      crates.append(this_line)
    else:
      instr = line.split()
      instructions.append(list(map(int, filter(lambda t: t.isnumeric(), instr))))
crates.pop()
instructions.pop(0)

crates_new = []
crates_rot = zip(*reversed(crates))
for line in crates_rot:
  this = []
  for x in line:
    if x != '':
      this.append(x)
  crates_new.append(this)

for line in instructions:
  crates_moving = []
  num_to_move = line[0]
  move_from = line[1]-1
  move_to = line[2]-1
  for i in range(num_to_move,0,-1):
    crates_moving.append(crates_new[move_from].pop())
  crates_moving.reverse()
  for x in crates_moving:
    crates_new[move_to].append(x)
  crates_moving.clear()

for line in crates_new:
  print(line)