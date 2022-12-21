import string
input = [x for x in (open('input.txt', 'r').read().splitlines())]
alphabet = list(string.ascii_letters)
sum_1, sum_2 = 0, 0

# Part 1
for line in input:
  comps = [line[:int(len(line)/2)],line[int(len(line)/2):]]
  for letter in alphabet:
    if letter in comps[0] and letter in comps[1]:
      sum_1 += alphabet.index(letter)+1
      break

# Part 2
for i in range(0,len(input),3):
  lines = [input[i],input[i+1],input[i+2]]
  for letter in alphabet:
    if letter in lines[0] and letter in lines[1] and letter in lines[2]:
      sum_2 += alphabet.index(letter)+1
      break

print(f'Part 1: {sum_1}')
print(f'Part 2: {sum_2}')

  