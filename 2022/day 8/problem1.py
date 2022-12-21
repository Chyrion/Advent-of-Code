input = [x for x in (open('input.txt', 'r').read().splitlines())]
total_trees = 0
found_trees = []

# Found trees: Tuple(number, (row, index in row))
# Adapt to columns with: (number, (index in col, col number))

# rows
for row in input:
  r_num = input.index(row)

  max = -1
  for i in range(len(row)):
    num = int(row[i])
    num_tuple = (num, (r_num,i))
    if num > max:
      max = num
      if num_tuple not in found_trees:
        found_trees.append(num_tuple)

  max = -1
  for i in range(len(row)-1,0,-1):
    num = int(row[i])
    num_tuple = (num, (r_num,i))
    if num > max:
      max = num
      if num_tuple not in found_trees:
        found_trees.append(num_tuple)

columns = []

for i in range(len(input[0])):
  this_c = []
  for c in range(len(input)):
    this_c.append(int(input[c][i]))
  columns.append(this_c)

# columns
for col in columns:
  c_num = columns.index(col)

  max = -1
  for i in range(len(col)):
    num = int(col[i])
    num_tuple = (num, (i, c_num))
    if num > max:
      max = num
      
      if num_tuple not in found_trees:
        total_trees += 1
        found_trees.append(num_tuple)

  max = -1
  for i in range(len(col)-1,0,-1):
    num = int(col[i])
    num_tuple = (num, (i, c_num))
    if num > max:
      max = num
      
      if num_tuple not in found_trees:
        total_trees += 1
        found_trees.append(num_tuple)

print(found_trees)
print(len(found_trees))
    