with open('input1.txt', 'r') as f:
  _in = f.read()
  bits = _in.splitlines()
  f.close()

def binToDec(b):
  p, t = 1, 0
  for f in range(len(b)):
    if b[f] == 1:
      t = t + p
    p = p * 2
  return t

zeros, ones, comp, l0, l1, ox, co = [], [], [], [], [], [], []

for i in range(0, 12):
  zeros.append(0), ones.append(0), ox.append(0), co.append(0)

for bin in bits:
  nums = [char for char in bin]
  for i, n in enumerate(nums):
    if n == '0':
      zeros[i] = zeros[i] + 1
    else:
      ones[i] = ones[i] + 1
  comp.append(nums)

for i in range(len(comp)):
  zero, one = False, False
  for x in range(len(comp[i])):
    zero, one = False, False
    if ones[i] == zeros[i] or ones[i] > zeros[i]:
      one = True
    else:
      zero = True
    if one:
      if comp[i][x]


defbits = []
print(comp[0][1])


# print(f'defbits: {defbits}')