# same concept as for problem 1, but kinda inverse
# check for correct pair etc etc

input = [x for x in (open('input.txt', 'r').read().splitlines())]

opens = ['(', '[', '{', '<']
closes = [')', ']', '}', '>']
scores = []

for line in input:
  check = ''
  completer = ''
  corrupt = False
  i = 0
  for l in range(len(line)):
    check += line[l]
    if check[i] in opens:
      i += 1
    elif check[i] in closes:
      symInd = closes.index(check[i])
      if check[i-1] == opens[symInd]:
        check = check[:-2]
        i -= 2
      else: 
        corrupt = True
        break
      i += 1
  if corrupt == False:
    _score = 0
    for x in range(len(check)-1, -1, -1):
      symType = opens.index(check[x])
      completer += closes[symType]
      _score = (_score * 5) + (symType + 1)
    scores.append(_score)

scores.sort()

print(scores[len(scores)//2])