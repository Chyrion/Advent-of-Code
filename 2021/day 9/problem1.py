# go through each point in 2d list
# check if the value has lower values around it
# if yes, ignore and move on
# if not, add to list of low points

# doesnt work lol

input = [[int(x) for x in y] for y in (open('input.txt', 'r').read().splitlines())]
lows = []

def neighbors(n, x, y):
  isLow = False
  smallers = 4
  try:
    if n < input[x-1][y]:
      smallers -= 1
    if n < input[x+1][y]:
      smallers -= 1
    if n < input[x][y+1]:
      smallers -= 1
    if n < input[x][y-1]:
      smallers -= 1
  except:
    smallers -= 1

  if smallers == 0:
    isLow = True
    
  return isLow
  # if x == 0 and y == 0:
  #   isLow = n < input[y+1][x] or n < input[y][x+1]
  # elif x == 0:
  #   isLow = n < input[y-1][x] or n < input[y+1][x] or n < input[y][x+1]
  # elif x == len(input[0])-1:
  #   isLow = n < input[y-1][x] or n < input[y+1][x] or n < input[y][x-1]
  # elif y == 0:
  #   isLow = n < input[y][x-1] or n < input[y][x+1] or n < input[y+1][x]
  # elif y == len(input)-1:
  #   isLow = n < input[y-1][x] or n < input[y][x+1] or n < input[y][x-1]
  # elif x == len(input[0])-1 and y == len(input)-1:
  #   isLow = n < input[y-1][x] or n < input[y][x-1]
  # elif y == 0 and x == len(input[0])-1:
  #   isLow = n < input[y][x-1] or n < input[y+1][x]
  # elif x == 0 and y == len(input)-1:
  #   isLow = n < input[y-1][x] or n < input[y][x+1]


for y in range(len(input)):
  for x in range(len(input[0])):
    if neighbors(input[y][x], x, y):
      lows.append(input[y][x]+1)

print(sum(lows))
