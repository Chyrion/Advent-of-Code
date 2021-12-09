raw = [x for x in (open('input.txt', 'r').read().splitlines())]
common = ''
for entry in raw:
  for ent in raw:
    numOfMatches = 0
    if entry != ent:
      matched_chars = [ent[i] if ent[i] == entry[i] else None for i in range(len(ent))]
      for x in matched_chars:
        if x != None:
          numOfMatches += 1
      if numOfMatches == len(entry) - 1:
        for i in range(len(entry)):
          if entry[i] == ent[i]:
            common += entry[i]
    if len(common) == len(entry) - 1:
      break
  if len(common) == len(entry) - 1:
      break

print(common)