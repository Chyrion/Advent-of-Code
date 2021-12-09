raw = [x for x in (open('input.txt', 'r').readlines())]
lines = [[x for x in (raw[i].split())] for i in range(len(raw))]
print(sum([x for sub in [[1 for i in range(11,15) if len(ent[i]) in [2, 3, 4, 7]] for ent in lines] for x in sub]))

#numOf1478 = 0
#for ent in lines:
#  for i in range(11,15):
#    if len(ent[i]) == 2 or len(ent[i]) == 3 or len(ent[i]) == 4 or len(ent[i]) == 7:
#      numOf1478 += 1
#print(numOf1478)