from collections import defaultdict
input = open('input.txt', 'r').read()
base_str = ''
version_total = 0

#input = 'A0016C880162017C3686B18A3D4780'
#input = 'EE00D40C823060'
hex_to_bin = dict({
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111'})

for c in input:
  base_str += hex_to_bin[c]

def parseLiteral(data):
  vals = ''
  groups = defaultdict(str)
  for n in range(100):
    while len(groups[n]) < 5:
      groups[n] += data[0]
      data = data[1:]
    if groups[n][0] == '0':
      break
  print(groups)
  for n in groups.values():
    vals += n[1:5]
  val = int(vals, 2)
  return data

def parseOperator(data):
  length_id = data[0]
  data = data[1:]
  if length_id == '0':
    print('operator has length type ID 0')
    length_subs = int(data[:15])
    data = data[15:]
    packets = data[:length_subs]
    while len(packets) != 0:
      data = typeDefine(packets)
    data = data[length_subs:]
  elif length_id == '1':
    num_packets = int(data[:11], 2)
    print('operator has length type ID 1')
    data = data[11:]
    for i in range(num_packets):
      data = typeDefine(data)
  return data

def typeDefine(_data):
  global version_total
  data = _data
  version_total += int(data[:3], 2)
  data = data[3:]
  type_id = int(data[:3], 2)
  data = data[3:]
  if type_id == 4:
    print('found literal')
    return parseLiteral(data)
  else:
    print('found operator')
    return parseOperator(data)
  return data

print(base_str)
typeDefine(base_str)
print(version_total)
