raw = [int(x) for x in (open('input.txt', 'r').read().split(','))]
print(min([sum([abs(val - i) for val in raw]) for i in range(max(raw))]))
#print(min([sum([abs(val - i) for val in [int(x) for x in (open('input.txt', 'r').read().split(','))]]) for i in range(max([int(x) for x in (open('input.txt', 'r').read().split(','))]))]))