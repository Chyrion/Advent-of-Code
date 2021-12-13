with open('input.txt', 'r') as f:
  raw = f.read().split('\n\n')
  dots_raw = raw[0].splitlines()
  dots = [[int(x) for x in dots_raw[i].split(',')] for i in range(len(dots_raw))]
  instructions_raw = [x for x in raw[1].split('\n')]
  instructions = [[x for x in (instructions_raw[i].split()[2].split('='))] for i in range(len(instructions_raw))]

def fold():
  for x in range(len(instructions)):
    fold_dir, fold_pos = instructions[x][0], int(instructions[x][1])
    if fold_dir == 'x':
      for i in range(len(dots)-1,-1,-1):
        if dots[i][0] > fold_pos:
          dist_from_fold = dots[i][0] - fold_pos
          if [fold_pos - dist_from_fold, dots[i][1]] not in dots:
            dots[i] = [fold_pos - dist_from_fold, dots[i][1]]
          else:
            dots.pop(i)
    elif fold_dir == 'y':
      for i in range(len(dots)-1,-1,-1):
        if dots[i][1] > fold_pos:
          dist_from_fold = dots[i][1] - fold_pos
          if [dots[i][0], fold_pos - dist_from_fold] not in dots:
            dots[i] = [dots[i][0], fold_pos - dist_from_fold]
          else:
            dots.pop(i)

# this gives a visual representation of the answer in the shell/terminal
def tabler():
  table = []
  xmax, ymax = 0, 0
  for i in range(len(dots)):
    if dots[i][0] > xmax:
      xmax = dots[i][0]
    if dots[i][1] > ymax:
      ymax = dots[i][1]
  for y in range(ymax+1):
    table.append([])
    for x in range(xmax+1):
      if [x, y] in dots:
        table[y].append('#')
      else:
        table[y].append(' ')
  for i in range(len(table)):
    s = ''
    for x in table[i]:
      s += x
    print(s)

fold()
tabler()