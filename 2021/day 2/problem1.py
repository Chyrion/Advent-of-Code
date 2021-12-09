with open('input1.txt', 'r') as f:
  _inst = f.read()
  inst = _inst.splitlines()
  f.close()

forward = 0
vert = 0

for move in inst:
  dir = move.split(' ')
  if (dir[0] == 'forward'):
    forward = forward + int(dir[1])
  elif (dir[0] == 'up'):
    vert = vert - int(dir[1])
  else:
    vert = vert + int(dir[1])
print(f'horizontal: {forward}\nvertical: {vert}')
total = forward * vert
print(total)