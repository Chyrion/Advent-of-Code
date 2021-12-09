alphabet = 'abcdefghijklmnopqrstuvwxyz'

raw = [x for x in (open('input.txt', 'r').read().splitlines())]

strings_twochars, strings_threechars = [], []

for entry in raw:
  chars = [char for char in entry]
  charcounter = [[alphabet[a], chars.count(alphabet[a])] for a in range(len(alphabet))]
  for i in range(len(charcounter)):
    if charcounter[i][1] == 2 and entry not in strings_twochars:
      strings_twochars.append(entry)
    if charcounter[i][1] == 3 and entry not in strings_threechars:
      strings_threechars.append(entry)

print(f'twos: {len(strings_twochars)}, threes: {len(strings_threechars)} ')
print(f'checksum: {len(strings_twochars) * len(strings_threechars)} ')
  #print(f'{entry}, charcounter: {charcounter} ')

