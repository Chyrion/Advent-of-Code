# Input:
# Player 1 starting position: 10
# Player 2 starting position: 8

pos1, pos2, score_p1, score_p2, roll = 10, 8, 0, 0, 0


while True:
  for i in range(1,101):
    roll += 1
    if i % 2 == 1:
      for x in range(3):
        pos1 += (i*3)-x
      while pos1 > 10:
        pos1 -= 10
      score_p1 += pos1
      print(score_p1)
      if score_p1 >= 1000:
        break
    if i % 2 == 0:
      for x in range(3):
        pos2 += (i*3)-x
      while pos2 > 10:
        pos2 -= 10
      score_p2 += pos2
      print(score_p2)
      if score_p2 >= 1000:
        break
  if score_p1 >= 1000:
    break
  elif score_p2 >= 1000:
    break

print(min([score_p1, score_p2]) * (roll*3))