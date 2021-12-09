raw = [x for x in (open('input.txt', 'r').read().splitlines())]
common = ''
for entry in raw: # get a string from input
  for ent in raw: # get another string from input for comparing
    numOfMatches = 0 # set number of matches between the two strings to 0
    if entry != ent: # make sure the two strings aren't the same
      matched_chars = [] # create empty list for matching characters
      for i in range(len(ent)): # loop with the length of the strings (same length so doesn't matter)
        if ent[i] == entry[i]: # check if the two strings are equivalent
          matched_chars.append(ent[i]) # if yes, put the character into the list
        else:
          matched_chars.append(None) # if not, append None to display no match

      for x in matched_chars: # loop through each element in the matched character list
        if x != None: # if the element is not None (aka, the element is a char), add to the number of matches
          numOfMatches += 1

      if numOfMatches == len(entry) - 1: # check for correct amount of matches between the two strings
        for i in range(len(entry)): # loop with length of string
          if entry[i] == ent[i]: # if the char matches, add it to the 'common' string
            common += entry[i]
  
  if len(common) == len(entry) - 1: # checks if the length of the string of common chars is correct
      break # breaks the main loop if all is okay

print(common)