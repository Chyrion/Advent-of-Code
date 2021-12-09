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

zeros, ones, gamma_bin, epsilon_bin = [], [], [], []
gammarate, epsilonrate = 0, 0

for i in range(0, 12):
  zeros.append(0), ones.append(0), gamma_bin.append(0), epsilon_bin.append(0)

for bin in bits:
  nums = [char for char in bin]
  for i, n in enumerate(nums):
    if n == '0':
      zeros[i] = zeros[i] + 1
    else:
      ones[i] = ones[i] + 1

for a in range(0, 12):
  if zeros[a] > ones[a]:
    gamma_bin[a] = 0
    epsilon_bin[a] = 1
  else:
    gamma_bin[a] = 1
    epsilon_bin[a] = 0

gamma_bin.reverse()
epsilon_bin.reverse()
gammarate = binToDec(gamma_bin)
epsilonrate = binToDec(epsilon_bin)
final = gammarate * epsilonrate

print(f'zeroes: {zeros}\nones: {ones}\ngamma rate: {gammarate}\nepsilon rate: {epsilonrate}\nfinal: {final}')