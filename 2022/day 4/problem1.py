input = [x.split(',') for x in (open('input.txt','r').read().splitlines())]
parsed = []
for assignment in input:
  this = []
  for a in assignment:
    ass = a.split('-')
    this.append((int(ass[0]),int(ass[1])))
  parsed.append(this)

total_1, total_2 = 0, 0


# Part 1
for nums in parsed:
  if (nums[0][0] <= nums[1][0] and nums[0][1] >= nums[1][1]) or (nums[1][0] <= nums[0][0] and nums[1][1] >= nums[0][1]):
    total_1 += 1

# Part 2
# This could've been done very similarly to part 1, but for fun, I wanted to do it differently
# and I had a dumb and inefficient idea for it so I went through with it
for nums in parsed:
  range_1, range_2 = [], []
  ok = False
  for i in range(nums[0][0],nums[0][1]+1):
    range_1.append(i)
  for i in range(nums[1][0],nums[1][1]+1):
    range_2.append(i)

  for n in range_1:
    if n in range_2:
      total_2 += 1
      ok = True
      break
  if not ok:
    for n in range_2:
      if n in range_1:
        total_2 += 1
        break

print(f'Part 1: {total_1}')
print(f'Part 2: {total_2}')
