raw = [x for x in (open('input.txt', 'r').read().splitlines())]

# 2D list edges >:(
raw.insert(0, [0 for i in range(len(raw[1])+2)])
raw.append([0 for i in range(len(raw[1])+2)])
for i in range(1, len(raw)-2):
  l = raw[i].split()
  l.insert(0, 0)
  l.append(0)
  raw[i] = "".join(map(str, l))

risktotal = 0
xmax, ymax = len(raw[0])-2, len(raw)-2
print((xmax, ymax))

def rightRisk(_x, y):
  risk, div = 0, 0
  x = _x+1
  dist = abs(x-xmax)+abs(y-ymax)
  if dist == 1:
    right = [(x,y)]
  elif x == xmax or y == ymax-1:
    right = [(x,y),(x+1,y),(x,y+1)]
  else:
    right = [(x,y-1),(x+1,y-1),(x,y),(x+1,y),(x,y+1),(x+1,y+1)]
  for n in right:
    if int(raw[n[1]][n[0]]) != 0:
      risk += int(raw[n[1]][n[0]])
      div += 1
  if div == 0:
    return 999
  else:
    (print(f'right risk: {risk} / {div} '))
    risk = risk/div
    return risk

def downRisk(x, _y):
  risk, div = 0, 0
  y = _y+1
  dist = abs(x-xmax)+abs(y-ymax)
  if dist == 1:
    down = [(x,y)]
  elif x == xmax-1 or y == ymax:
    down = [(x,y),(x+1,y),(x,y+1)]
  else:
    down = [(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
  for n in down:
    if int(raw[n[1]][n[0]]) != 0:
      risk += int(raw[n[1]][n[0]])
      div += 1
  if div == 0:
    return 999
  else:
    (print(f'down risk: {risk} / {div} '))
    risk = risk/div
    return risk

posx, posy = 1, 1
x_fin, y_fin, total_fin = False, False, False


while total_fin == False:
  print('current:')
  print((posx, posy),(int(raw[posy][posx])), risktotal)
  print('')

  right_risk = rightRisk(posx, posy)

  down_risk = downRisk(posx, posy)
  print((right_risk, down_risk))
  
  if (posx, posy) == (xmax-1, ymax):
    posx += 1
  elif (posx, posy) == (xmax, ymax-1):
    posy += 1
  elif right_risk < down_risk:
    posx += 1
  elif down_risk < right_risk:
    posy += 1
  elif right_risk == right_risk:
    if raw[posy][posx+1] < raw[posy+1][posx]:
      posx += 1
    elif raw[posy][posx+1] > raw[posy+1][posx]:
      posy += 1
    else:
      posy += 1
  
  x_fin if posx == xmax else False
  y_fin if posy == ymax else False
  total_fin if x_fin and y_fin else False
  risktotal += int(raw[posy][posx])
  print('new:')
  print((posx, posy),(int(raw[posy][posx])), risktotal)
  print('')

print(risktotal)