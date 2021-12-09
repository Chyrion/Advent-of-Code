raw = [int(x) for x in (open('input.txt', 'r').read().split(','))]
fuelPosits = [sum([((abs(val-i)**2)+abs(val-i))/2 for val in raw]) for i in range(max(raw))]
print(f'fuel needed: {min(fuelPosits)}')


#minFuelPosits = [sum(raw)*5555555]
#for i in range(max(raw)):
  # currFuelPosits = [((abs(val-i)**2)+abs(val-i))/2 for val in raw]
  # if sum(minFuelPosits) > sum(currFuelPosits):
  #   minFuelPosits = currFuelPosits
# print(minFuelPosits)