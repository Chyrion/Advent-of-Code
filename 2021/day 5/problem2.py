from collections import Counter, defaultdict

with open('input.txt', 'r') as f:
  raw = f.read().splitlines()
  points = defaultdict()
  for line in raw:
    s = line.split()
    points[raw.index(line)] = ([int(x) for x in s[0].split(',')], [int(x) for x in s[2].split(',')])

lines = defaultdict(int)

for n, pts in points.items():
  if pts[0][0] == pts[1][0]: # x1 = x2 -> vertical line
    x = pts[0][0]
    ymin, ymax = min([pts[0][1], pts[1][1]]), max([pts[0][1], pts[1][1]])
    for y in range(ymin, ymax+1):
      lines[(x, y)] += 1
  elif pts[0][1] == pts[1][1]: # y1 = y2 -> horizontal line
    y = pts[0][1]
    xmin, xmax = min([pts[0][0], pts[1][0]]), max([pts[0][0], pts[1][0]])
    for x in range(xmin, xmax+1):
      lines[(x, y)] += 1
  else: # diagonal lines
    xmin, xmax = min([pts[0][0], pts[1][0]]), max([pts[0][0], pts[1][0]])
    if xmin in pts[0]:
      y1, y2 = pts[0][1], pts[1][1]
      ys = int((y2-y1)/(xmax-xmin))
      for x in range(xmin, xmax+1):
        y = y1+int(ys*(x-xmin))
        lines[(x, y)] += 1
    if xmin in pts[1]:
      y1, y2 = pts[1][1], pts[0][1]
      ys = int((y2-y1)/(xmax-xmin))
      for x in range(xmin, xmax+1):
        y = y1+int(ys*(x-xmin))
        lines[(x, y)] += 1

intersections = 0
for val in lines.values():
  if val >= 2:
    intersections += 1
print(intersections)