with open('input_ex.txt', 'r') as f:
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
def router(currRoute, currBlocks, doubled, dubcount, routs):
  possibles = options(currRoute[len(currRoute)-1], currBlocks)
  rts = [currRoute]
  routes = routs
  if len(possibles) != 0:
    for i in range(len(possibles)):
      rts.append(currRoute + [possibles[i]])
    for a in range(1, len(rts)):
      if 'end' not in rts[a]:
        b = []
        for x in range(1, len(rts[a])):
          dubs = dubcount
          dubs = rts[a].count(doubled)
          if rts[a][x].islower():
            if rts[a][x] != doubled:
              b.append(rts[a][x])
            else:
              if dubs == 2:
                b.append(rts[a][x])
        #print(f'routing {rts[a]}\nblocks: {b}\ndoubled: {doubled} ({dubs} so far) ')
        router(rts[a], b, doubled, dubs, routes)
      else:
        if rts[a] not in routes:
          #print(rts[a])
          routes.append(rts[a])
  else:
    for x in range(len(routes)):
      combinations.append(routes[x])
    routes.clear()


        
# run the whole damn thing
def yep():
  opens = start()
  for a in range(len(opens)):
    rt = []
    rt = opens[a]
    router(rt, [], None, 0, [])

yep()
print(len(combinations))