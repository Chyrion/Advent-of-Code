with open('input1.txt', 'r') as f:
  raw = f.readlines()
  raw = [[x for x in (raw[i].split())] for i in range(len(raw))]
  #raw = [[raw[i].remove('->')] for i in range(len(raw))]
  print(raw)
  for i in range(len(raw)):
    raw[i].remove('->')
  lines = [[[int(x) for x in (raw[b][0].split(','))], [int(x) for x in (raw[b][1].split(','))]] for b in range(len(raw))]
  print(lines)
#[int(i) for i in list]