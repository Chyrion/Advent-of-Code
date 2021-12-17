from collections import defaultdict
#input = open('input.txt', 'r').read()
base_str = ''
version_total, num_packets, ops = 0, 0, 0
ops = defaultdict(int)
literals = []

def binToDec(b):
  # I have pre-existing function for this, but it's not here because i'm lazy

#input = 'A0016C880162017C3686B18A3D4780'
#input = 'EE00D40C823060'

def parseLiteral():
  global base_str
  global version_total
  init_len = len(base_str)
  vals = []
  version_total += binToDec(base_str[:3])
  base_str = base_str[6:]
  num_groups = 1
  groups = defaultdict(str)
  groups[1] = base_str[0]
  while groups[len(groups)][0] != 0:
    if len(groups[num_groups]) < 5:
      groups[num_groups] = base_str[:5]
    base_str = base_str[5:]
    if groups[num_groups][0] == '0':
      break
    else:
      num_groups += 1
  d = init_len-len(base_str)
  g = 0
  while (d+g) % 4 != 0: # count how many extra numbers are left over and delete them from the base
    g += 1
  base_str = base_str[g-1:]
  for n in groups.values():
    vals.append(n[1:])
  val = binToDec(''.join(map(str, vals)))
  print(val)
  typeDefine()

def parseOperator():
  global base_str
  global version_total
  length_id = base_str[6]
  version_total += binToDec(base_str[:3])
  base_str = base_str[7:]
  if length_id == '0':
    print(f'operator has length type ID {length_id} ')
    length_subs = binToDec(base_str[:15])
    base_str = base_str[15:]
    typeDefine()
  elif length_id == '1':
    print(f'operator has length type ID {length_id} ')
    global num_packets
    num_packets = binToDec(base_str[:11])
    base_str = base_str[11:]
    typeDefineCount(num_packets)

def typeDefine():
  global base_str
  if base_str[:4] == '0000':
    base_str = base_str[5:]
  if len(base_str) > 6:
    print(base_str)
    type_id = binToDec(base_str[3:6])
    if type_id == 4:
      print('found literal')
      parseLiteral()
    else:
      print('found operator')
      parseOperator()
  else:
    print('done')

def typeDefineCount(c):
  global base_str
  type_id = binToDec(base_str[3:6])
  if type_id == 4:
    print('found literal')
    parseLiteral()
  else:
    print('found operator')
    parseOperator()


typeDefine()
print(version_total)
