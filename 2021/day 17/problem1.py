# input: target area: x=248..285, y=-85..-56

targetxmin, targetxmax = 248, 285 
targetymin, targetymax = -85, -56
ymax, vels = 0, 0

def step(inx, iny):
  global ymax, vels
  (posx, posy), vx, vy, maxy = (0, 0), inx, iny, 0
  hit = False
  while True:
    (posx, posy) = (posx+vx, posy+vy)
    if vx > 0:
      vx -= 1
    vy -= 1
    if posy > maxy:
      maxy = posy
    if posy < targetymin or targetxmax < posx:
      break
    if posx in range(targetxmin, targetxmax+1): # range upper bound is exclusive so +1 to make it inclusive to actual bounds
      if posy in range(targetymin, targetymax+1):
        hit = True
        break
  if hit == True:
    vels += 1
    if maxy > ymax:
      ymax = maxy

for x in range(300): 
  for y in range(-100, 85):
    step(x, y)

print(f'part 1: {ymax}')
print(f'part 2: {vels} ')

# I initially had my for loop bounds set to x=1000, y=-500,1000. However, after some thinking, the bounds for this can be determined quite easily
# For x, all you need is for the initial x velocity to not be over the target's maximum x. If it is over, it will just overshoot right away 
# Here, I could have it on 285, but 300 is neater.
# For y, the lower bound follows the same concept as for x, and the upper bound is just the abs of that value. Because:
# The probe is launched from y=0. With vY (y velocity) decreasing by 1 every step, vY will eventually become 0, which marks the highest point
# (maximum of the parabola of launch, tangent slope = 0). From here, vY will keep decreasing with the same steps.
# Since the way down is the exact same as the way up in terms of vY but going down instead of up, the y position will eventually equal to 0.
# Thus, every launch with an initial vY > 0 will have y=0 as one point. The requirement from here (for the upper bound)
# is that the y position in the next step will be equal to the lower bounds of the target y. Thus, with my lower bound at -85,
# vY at y=0 should be -85. This shows us that the upper bound of initial vY is abs(-85) = 85
# Actually lol its not, it's 84 (for loop upper bound is exclusive, so in there 85 is correct)
# I might know what it's about with the way down being 'offset' by one step but I don't know if that's true
# But I'm close tho
