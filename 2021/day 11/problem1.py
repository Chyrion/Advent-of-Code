from collections import defaultdict

input = [[int(x) for x in y] for y in (open('input.txt', 'r').read().splitlines())]

# Same approach for managing the edges of a 2d list as in day 9 (add a ring of None around the list)
# Don't know yet how to handle the edges in any other nice way :(
input.insert(0, [None for i in range(len(input[1])+2)])
input.append([None for i in range(len(input[1])+2)])
for i in range(1, len(input)):
  input[i].insert(0, None)
  input[i].append(None)

flashes = defaultdict(int)
flashes['count'] = 0 # using a defaultdict for this because using a single variable was not working for whatever reason
flashed = defaultdict(bool)

def addToNeighbors(x, y): # add 1 to each neighbor, accounting for their flash status
  neighbors = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
  for n in neighbors:
    if input[n[0]][n[1]] != None and flashed[(n[1], n[0])] == False:
      input[n[0]][n[1]] += 1

def phase1(): # increase energy of each octopus
  for y in range(1, len(input)-1):
    for x in range(1, len(input[0])-1):
      input[y][x] += 1
  phase2() # once done, move to flashing

def flash(x, y): # flash function, which checks if the input value is above 9 and flashes as necessary
  if input[y][x] > 9 and flashed[(x, y)] == False:
    flashed[(x, y)] = True
    addToNeighbors(x, y)
    input[y][x] = 0

def phase2(): # flashes
  for y in range(1, len(input)-1):
    for x in range(1, len(input[y])-1):
      flash(x, y) # do a flash check for each entry
  c9 = 0
  for y in range(1, len(input)-1):
    for x in range(1, len(input[y])-1):
      if input[y][x] > 9: # go through each entry and see if there are any above 9
        c9 += 1
  phase2() if c9 != 0 else phase3() # repeat phase 2 if there are values above 9, in order to create each possible flash, else move on

def phase3(): # set each flasher to 0 and count flashes
  for y in range(1, len(input)-1):
    for x in range(1, len(input[0])-1):
      if flashed[(x, y)] == True:
        flashes['count'] += 1
        flashed[(x, y)] = False
        input[y][x] = 0

for i in range(100): # run for i steps
  phase1()

print(flashes['count'])