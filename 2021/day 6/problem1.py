fishes = [[int(x) for x in (open('input1.txt', 'r').read().split(','))].count(i) for i in range(9)]
for i in range(256):
  numOfZero = 0
  for x in range(9):
    if x != 0:
      fishes[x-1] += fishes[x]
      fishes[x] = 0
    else:
      numOfZero = fishes[0]
      fishes[0] = 0
  fishes[8] = numOfZero
  fishes[6] += numOfZero
print(sum(fishes))