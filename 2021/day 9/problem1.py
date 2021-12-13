# I don't know how to properly handle 2d list edges
# My workaround for that issue is adding an edge of None elements around the whole list
# This way, when you check edge neighbors, there's no need to deal with negative indices etc.
# 
# The method:
# go through each point in 2d list
# add the neighboring points to a list, if the neighbor is not None
# check if the point is lower than the min of the neighbor list
# if yes, add it to low points and calculate risk


input = [[int(x) for x in y] for y in (open('input.txt', 'r').read().splitlines())]
lows = []

input.insert(0, [None for i in range(len(input[1])+1)])
input.append([None for i in range(len(input[1])+1)])
for i in range(1, len(input)):
  input[i].insert(0, None)
  input[i].append(None)

for r in range(1, len(input)-1):
  for c in range(1, len(input[1])-1):
    neighbors = []
    print(f'row: {r}, col: {c}, num: {input[r][c]} ')
    if input[r-1][c] != None:
      neighbors.append(input[r-1][c])
    if input[r+1][c] != None:
      neighbors.append(input[r+1][c])
    if input[r][c-1] != None:
      neighbors.append(input[r][c-1])
    if input[r][c+1] != None:
      neighbors.append(input[r][c+1])
    if input[r][c] < min(neighbors):
      lows.append(input[r][c]+1)

print(sum(lows))

