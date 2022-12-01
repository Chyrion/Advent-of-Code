decimal = 607

def decToBin(dec):
  bin = ''
  decim_div = dec
  while (decim_div >= 1):
    bin += str(decim_div % 2)
    decim_div = decim_div // 2
  return bin

print(decToBin(decimal))