with open('input1.txt', 'r') as f:
  _inst = f.read()
  inst = _inst.splitlines()
  f.close()

horizontal = 0
depth = 0
aim = 0

for move in inst:
  dir = move.split(' ')
  if (dir[0] == 'forward'):
    horizontal = horizontal + int(dir[1])
    depth = depth + (aim * int(dir[1]))
  elif (dir[0] == 'up'):
    aim = aim - int(dir[1])
  else:
    aim = aim + int(dir[1])
print(f'horizontal: {horizontal}\ndepth: {depth}\naim: {aim}')
total = horizontal * depth
print(total)