# Answer 1: 1853
# Answer 2: 72706

def determineMax(gameResults):
  """
    Determines maxs number of each types for one game.
    
      Parameters:
              gameResults (array<string>): Array of draws for a single game

      Returns:
              gameMaxs ((int, int, int)): Tuple containing greatest draw for red, green, then blue.
  """
  maxRed = 0
  maxBlue = 0 
  maxGreen = 0

  for gameDraw in gameResults:
    for colorAmount in gameDraw.split(','):
      textSplit = colorAmount.strip().split(" ")
      amount = int(textSplit[0])
      color = textSplit[1]

      if color.find("green") != -1 and maxGreen < amount:
        maxGreen = amount
      elif color.find("red") != -1 and maxRed < amount:
        maxRed = amount
      elif color.find("blue") != -1 and maxBlue < amount:
        maxBlue = amount
  return (maxRed, maxGreen, maxBlue)

def isGamePossible(gameMax, limitMax):
  """
    Checks if game was possible by comparing the number of possible cubes to the draws.

      Parameters:
        gameMax ((int, int, int)): Tuple containing the highest number of times a cube was found in a single game
        limitMax ((int, int, int)): Tuple containing the upper limit of cubes that could be in the bag
  """
  return gameMax[0] <= limitMax[0] and gameMax[1] <= limitMax[1] and gameMax[2] <= limitMax[2]

def main():
  file = open("input.txt", 'r')
  sumOfIds = 0
  sumOfPowers = 0 

  for line in file.readlines():
    sections = line.split(":")
    gameId = int(sections[0].split("Game ")[1])
    gameResults = sections[1].split(';')
    gameMax = determineMax(gameResults)
    
    # Part 1
    if isGamePossible(gameMax, [12, 13, 14]):
      sumOfIds = sumOfIds + gameId

    # Part 2
    sumOfPowers = sumOfPowers + (gameMax[0] * gameMax[1] * gameMax[2])

  print("Sum of Ids: ", sumOfIds)
  print("Sum of powers: ", sumOfPowers)


main();