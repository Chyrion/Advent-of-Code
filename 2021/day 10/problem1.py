# take each line, add the characters into a new string one by one
# check if the character is an opener or closer
# if opener, continue
# if closer, check the earlier characters to see if it is valid for closing
# if valid, delete the two characters which make up the syntax pair and continue with adding characters
# if invalid, add the corrupting character to list and break the loop for that line
#
# example:
# [[<[([]))<([[{}[[()]]]: Expected ], but found ) instead
# add [[<[([] <- closer, with a valid opener = valid -> delete pair -> continue
# [[<[() <- closer, valid -> delete, continue
# [[<[) <- closer, but invalid opener -> corrupt
# get corrupt symbol and add to corrupters

input = [x for x in (open('input.txt', 'r').read().splitlines())]

opens = ['(', '[', '{', '<']
closes = [')', ']', '}', '>']
corrupters = []
score = 0

for line in input:
  check = ''
  i = 0
  for l in range(len(line)):
    check += line[l]
    if check[i] in opens: # check if char is opener
      i += 1
    elif check[i] in closes: # check if char is closer
      symInd = closes.index(check[i]) # symbol index, used to get the corresponding opener symbol
      if check[i-1] == opens[symInd]: # if the previous character is the correct opener, delete the pair
        check = check[:-2]
        i -= 2 # go back 2 spots in the check string to account for deleted characters
      else: 
        print(f'{check[i-1]} and {check[i]} are not a match! corrupt, breaking loop ')
        corrupters.append(check[i])
        break
      i += 1

for c in corrupters:
  if c == ')':
    score += 3
  if c == ']':
    score += 57
  if c == '}':
    score += 1197
  if c == '>':
    score += 25137

print(score)
