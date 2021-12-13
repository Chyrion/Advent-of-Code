with open('input.txt', 'r') as f:
  raw = f.read().split('\n\n')
  dots_raw = raw[0].splitlines()
  dots = [[int(x) for x in dots_raw[i].split(',')] for i in range(len(dots_raw))]
  instructions_raw = [x for x in raw[1].split('\n')]
  instructions = [[x for x in (instructions_raw[i].split()[2].split('='))] for i in range(len(instructions_raw))]
  # input parsing could be more compact, but it's more clear to have it opened up

def fold():
  fold_dir, fold_pos = instructions[0][0], int(instructions[0][1])
  if fold_dir == 'x':
    for i in range(len(dots)-1,-1,-1):
      if dots[i][0] > fold_pos:
        dist_from_fold = dots[i][0] - fold_pos
        if [fold_pos - dist_from_fold, dots[i][1]] not in dots:
          dots[i] = [fold_pos - dist_from_fold, dots[i][1]]
        else:
          dots.pop(i)
  # for my input, the 'y' section is useless but it's here just to show it could do both
  elif fold_dir == 'y':
    for i in range(len(dots)-1,-1,-1):
      if dots[i][1] > fold_pos:
        dist_from_fold = dots[i][1] - fold_pos
        if [dots[i][0], fold_pos - dist_from_fold] not in dots:
          dots[i] = [dots[i][0], fold_pos - dist_from_fold]
        else:
          dots.pop(i)  

fold()
print(len(dots))