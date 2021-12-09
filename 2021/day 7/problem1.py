raw = [int(x) for x in (open('input.txt', 'r').read().split(','))]
fuelPosits = [sum([abs(val - i) for val in raw]) for i in range(max(raw))]
print(min(fuelPosits))