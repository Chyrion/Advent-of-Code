with open('input1.txt', 'r') as f:
  inp = f.readlines()
  draw = [int(x) for x in (inp[0].split(','))]
  inp.pop(0)

boards_raw = list(filter(None, [[int(x) for x in inp[i].split()] for i in range(len(inp))]))
boards, checkboards, wincard = [], [], []
win = False
win_num, winCardNum, sum = 0, 0, 0

for i in range(0, len(boards_raw), 5):
  boards.append([[x for x in boards_raw[i+b]] for b in range(5)])

for i in range(len(boards)):
  checkboards.append([[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]) # bleh

while sum == 0:
  for num in draw:
    for i in range(len(boards)):
      card = boards[i]
      ind = None
      rw, cardNum, col = 0, 0, 0
      found = any(num in sublist for sublist in card)
      if found:
        while ind == None:
          try:
            ind = card[rw].index(num)
            cardNum = boards.index(card)
            checkboards[cardNum][rw][ind] = card[rw][ind]
          except:
            rw += 1
        col = 0
        for r in range(5):
          if checkboards[cardNum][r][ind] == card[r][ind]:
            col += 1
        if checkboards[cardNum][rw] == card[rw] or col == 5:
          for r in range(5):
            for c in range(5):
              if checkboards[cardNum][r][c] == None:
                sum += card[r][c]
          print(f'sum of unmarked: {sum}, multiplied by winner number {num}: {sum * num} ')
          win = True
          break
      if win:
        break
    if win:
      break 