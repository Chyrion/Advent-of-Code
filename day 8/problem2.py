raw = [x for x in (open('input.txt', 'r').readlines())]
lines = [[x for x in (raw[i].split())] for i in range(len(raw))]
#segments = ['012456', '25', '02346', '02356', '1235', '01356', '013456', '025', '0123456', '012356']
#numOf1478 = 0


def decodeSegment(entry, i, ref):
  segment = []
  ref_split = [char for char in ref]
  #.find()
  return segment

for ent in lines:
  currSegments = [[i, None] for i in range(10)]
  for i in range(10):
    if len(ent[i]) == 7:
      currSegments[8] = [8, ent[i]]
      print([char for char in currSegments[8][1]])
      break
  #for i in range(10):
  #  if i != 8:
  #    currSegments[i] = decodeSegment(ent[i], i, currSegments[8][1])
  #print(currSegments)
print()




# if len(ent[i]) == 2:
#   currSegments[1] = [1, ent[i]]
# if len(ent[i]) == 3:
#   currSegments[7] = [7, ent[i]]
# if len(ent[i]) == 4:
#   currSegments[4] = [4, ent[i]]