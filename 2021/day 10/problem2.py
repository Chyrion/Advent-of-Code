# same concept as for problem 1, but kinda inverse
# check if the line is corrupt or not

input = [x for x in (open('input.txt', 'r').read().splitlines())]

opens = ['(', '[', '{', '<']
closes = [')', ']', '}', '>']
scores = []

for line in input:
  check = ''
  corrupt = False
  i = 0
  for l in range(len(line)):
    check += line[l]
    if check[i] in closes:
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
    for x in range(len(check)-1, -1, -1): # loop through the remainder of the check string (all the existing correct syntax is removed)
      symType = opens.index(check[x]) # get index of the symbol from list
      _score = (_score * 5) + (symType + 1) # the score of a symbol is the index + 1, so calculating scores with that
    scores.append(_score)

scores.sort()
print(scores[len(scores)//2])