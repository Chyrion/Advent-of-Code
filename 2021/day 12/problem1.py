with open('input.txt', 'r') as f:
  _input = f.read().splitlines()
  input = [[x for x in _input[i].split('-')] for i in range(len(_input))] 

combinations = []

# get possible starts
def start():
  starts = []
  for i in range(len(input)):
    if input[i][0] == 'start':
      starts.append(['start', input[i][1]])
    elif input[i][1] == 'start':
      starts.append(['start', input[i][0]])
  return starts

# get available moves from this cave
def options(block, blocked):
  opts = []
  for i in range(len(input)):
    if block in input[i] and 'start' not in input[i]:
      ind = input[i].index(block)
      if input[i][ind-1] not in blocked:
        opts.append(input[i][ind-1])
  return opts

# creates the possible routes through recursion
# gets available options from the current cave and goes through each choice and checks viability
# if it finds a route that ends in an 'end' block, it adds it to the list of combinations
def router(currRoute, currBlocks):
  possibles = options(currRoute[len(currRoute)-1], currBlocks)
  rts = [currRoute]
  if len(possibles) != 0:
    for i in range(len(possibles)):
      rts.append(currRoute + [possibles[i]])
    for a in range(1, len(rts)):
      if 'end' not in rts[a]:
        b = []
        for x in range(1, len(rts[a])):
          if rts[a][x].islower():
            b.append(rts[a][x])
        router(rts[a], b)
      else:
        print(f'{rts[a]} added\n')
        combinations.append(rts[a])
        
# run the whole damn thing
def yep():
  opens = start()
  for a in range(len(opens)):
    rt = []
    rt = opens[a]
    router(rt, [])
    
  
yep()
print(len(combinations))