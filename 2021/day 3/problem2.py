from collections import Counter, defaultdict

with open('input1.txt', 'r') as f:
  bits = f.read().splitlines()

def binToDec(b):
  t = 0
  bl = list(reversed(list(b)))
  for i in range(len(bl)):
    t += int(bl[i])*(2**i)
  return t

oxygen, co2 = defaultdict(str), defaultdict(str)
for i in range(len(bits)):
  oxygen[i], co2[i] = bits[i], bits[i]


# oxygen:
for i in range(len(bits[0])):
  if len(oxygen) == 1:
    break
  else:
    CN = Counter()
    for bin in oxygen:
      CN.update(oxygen[bin][i])
    common = 0
    if CN['1'] >= CN['0']:
     common = 1
    temp = defaultdict(str)
    for key, bin in oxygen.items():
      if bin[i] == str(common):
        temp[key] = bin
    oxygen = temp

# co2
for i in range(len(bits[0])):
  if len(co2) == 1:
    break
  else:
    CN = Counter()
    for bin in co2:
      CN.update(co2[bin][i])
    common = 0
    if CN['1'] >= CN['0']:
     common = 1
    temp = defaultdict(str)
    for key, bin in co2.items():
      if bin[i] != str(common):
        temp[key] = bin
    co2 = temp

o, c = 0, 0
for val in oxygen.values():
  o = binToDec(val)

for val in co2.values():
  c = binToDec(val)
print(o*c)