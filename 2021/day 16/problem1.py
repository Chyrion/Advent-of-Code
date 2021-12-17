from collections import defaultdict

input = open('input.txt', 'r').read()

ver_tot = 0
base_str = ''
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

# def binToDec(b):
#   t = 0
#   bl = list(reversed(list(b)))
#   for i in range(len(bl)):
#     t += int(bl[i])*(2**i)
#   return t

def parse(data):
  global ver_tot
  print(f'parsing {data} ')
  ver_tot += int(data[:3], 2)
  data = data[3:]
  typeid = int(data[:3], 2)
  data = data[3:]
  if typeid == 4:
    print(f'literal')
    nums = defaultdict(str)
    for n in range(100):
      while len(nums[n]) < 5:
        nums[n] += data[0]
        data = data[1:]
      if nums[n][0] == '0':
        break
    num = ''
    for c in nums.values():
      num += c[1:]
    print(int(num, 2))
  else:
    lengthid = data[0]
    data = data[1:]
    if lengthid == '0':
      print('operator 0')
      len_subs = int(data[:15], 2)
      data = data[15:]
      subs = data[:len_subs]
      while subs:
        subs = parse(subs)
      data = data[len_subs:]
    else:
      num_subs = int(data[:11], 2)
      print('operator 1', num_subs)
      data = data[11:]
      for i in range(num_subs):
        data = parse(data)
  return data

#parse(base_str)
parse(base_str)
print(ver_tot)