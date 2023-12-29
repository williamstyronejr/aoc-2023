# Answer #1: 6942
# Answer #2:

def isValidMove(posX, posY, fromPos, diagram):
  if posX < 0 or posY < 0 or posX >= diagram.__len__() or posY >= diagram[0].__len__():
    return False
  char = diagram[posX][posY];

  if char == '.' or char == 'S':
    return False
  
  # Check directional movement
  if char == '|' and not (fromPos[0] == posX - 1 or fromPos[0] == posX + 1):
    return False
  elif char == '-' and not (fromPos[1] == posY - 1 or fromPos[1] == posY + 1):
    return False
  elif char == 'L' and not (fromPos[0] == posX - 1 or fromPos[1] == posY + 1):
    return False
  elif char == 'J' and not (fromPos[0] == posX - 1 or fromPos[1] == posY - 1):
    return False
  elif char == '7' and not (fromPos[0] == posX + 1 or fromPos[1] == posY - 1):
    return False
  elif char == 'F' and not (fromPos[0] == posX + 1 or fromPos[1] == posY + 1):
    return False
  
  return True

def determineNextMoves(pos, diagram):
  nextMoves = []

  currTile = diagram[pos[0]][pos[1]]
  if currTile == "S":
    if isValidMove(pos[0] -1, pos[1], pos, diagram):
      nextMoves.append((pos[0] -1, pos[1]))

    if isValidMove(pos[0] + 1, pos[1], pos, diagram):
      nextMoves.append((pos[0] + 1, pos[1]))

    if isValidMove(pos[0], pos[1] - 1, pos, diagram):
      nextMoves.append((pos[0], pos[1] - 1))

    if isValidMove(pos[0], pos[1] + 1, pos, diagram):
      nextMoves.append((pos[0], pos[1] + 1))

  elif currTile == '-':
    newPositions = [(pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
    for newPos in newPositions:
      if isValidMove(newPos[0], newPos[1], pos, diagram):
        nextMoves.append(newPos)
  
  elif currTile == '|': 
    newPositions = [(pos[0] - 1 , pos[1]), (pos[0] + 1, pos[1])]
    for newPos in newPositions:
      if isValidMove(newPos[0], newPos[1], pos, diagram):
        nextMoves.append(newPos)

  elif currTile == '7': 
    newPositions = [(pos[0] + 1, pos[1]), (pos[0], pos[1] - 1)]
    for newPos in newPositions:
      if isValidMove(newPos[0], newPos[1], pos, diagram):
        nextMoves.append(newPos)

  elif currTile == 'F':
    newPositions = [(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1)]
    for newPos in newPositions:
      if isValidMove(newPos[0], newPos[1], pos, diagram):
        nextMoves.append(newPos)

  elif currTile == 'L': 
    newPositions = [(pos[0] - 1, pos[1]), (pos[0], pos[1] + 1)]
    for newPos in newPositions:
      if isValidMove(newPos[0], newPos[1], pos, diagram):
        nextMoves.append(newPos)

  elif currTile == 'J': 
    newPositions = [(pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)]
    for newPos in newPositions:
      if isValidMove(newPos[0], newPos[1], pos, diagram):
        nextMoves.append(newPos)
  return nextMoves

def main():
  diagram = []
  startingPos = (0,0)
  farthestStep = 0
  posScores = dict()
  tilesEnclosed = 0
  outOfLoop = []

  with open ("input.txt", 'r') as file:
    for index, line in enumerate(file.readlines()):
      diagram.append([*line.strip()])
      outOfLoop.append(["I" for x in range(line.__len__())])
      sPos = line.find("S")
      if sPos != -1:
        startingPos = (index, sPos)
        outOfLoop[index][sPos] = "0"


  currentMoves = determineNextMoves(startingPos, diagram)
  posScores[f'{startingPos[0]},{startingPos[1]}'] = 0
  steps = 0

  while currentMoves.__len__() > 0:
    newMoves = []
    steps += 1

    for currMove in currentMoves:
      key = f'{currMove[0]},{currMove[1]}'
      
      if key in posScores and posScores[key] <= steps:
        continue
      outOfLoop[currMove[0]][currMove[1]] = "0"
      posScores[key] = steps
      newMoves.extend(determineNextMoves(currMove, diagram))
    
    currentMoves = newMoves
  


  print(outOfLoop)

  for stepCount in posScores.values():
    if farthestStep < stepCount:
      farthestStep = stepCount

  print(f"Part 1: Steps from starting to farthest: {farthestStep}")
  print(f"Part 2: Number of Tiles Enclosed: {tilesEnclosed}")

main()

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.