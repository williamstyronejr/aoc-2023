# Answer #1: 21158.0
# Answer #2: 6050769

import math

def main():
  file = open("input.txt", 'r')
  sum = 0
  numOfCards = 0
  cardRepeats = dict()

  for line in file.readlines():
    # Part 1
    titleSplit = line.split(":")
    cardNumber = int(titleSplit[0].split("Card ")[1])
    numberSplit = titleSplit[1].split("|")
    winningNumbers = set(numberSplit[0].strip().split(' '))
    numbersPicked = set(numberSplit[1].strip().split(' '))
    matches = numbersPicked.intersection(winningNumbers)
    matches.discard("")

    # Part 2
    numOfCards += 1 
    if cardNumber in cardRepeats:
      numOfCards += cardRepeats[cardNumber]

    if matches.__len__() > 0:
      # Part 1 
      sum += 1 * math.pow(2, matches.__len__() - 1)

      # Part 2
      for index in range(0, matches.__len__()):
        cardsToAdd = 1 if not cardNumber in cardRepeats else cardRepeats[cardNumber] + 1 
        
        if cardNumber + index + 1 in cardRepeats:
          cardRepeats[cardNumber + index + 1] += cardsToAdd
        else:
          cardRepeats[cardNumber + index + 1] = cardsToAdd

  print(f"Part 1 - Sum of Card's Worth: {sum}")
  print(f"Part 2 - Total Number of Card: {numOfCards}")

main()