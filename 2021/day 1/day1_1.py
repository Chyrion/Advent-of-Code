with open('day1_1_in.txt', 'r') as f:
  val_in = f.read()
  val_list = val_in.splitlines()
  f.close()
val_list = [int(i) for i in val_list]

# print(sum(x < y for x, y in zip(val_list, val_list[1:])))
inc = 0
for val in val_list:
  if val_list.index(val) == len(val_list):
    print('final element')
  #elif (val > val_list[val_list.index(val)-1]):
  elif val < val_list[val_list.index(val)+1]:
    print(inc)
    inc = inc + 1
print(inc)