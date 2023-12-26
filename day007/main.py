# Answer #1: 250347426
# Answer #2:

def compareRank(card1, card2): 
  """ 
    Returns {int} Returns -1 if card1 is greater than card 2 otherwise returns 1.
  """
  cardOrder = ['A','K','Q','J','T','9','8','7','6','5','4','3','2', 'J']

  if card1 == card2:
    return 0
  
  for index in range(0, card1.__len__()):
    if card1[index] == card2[index]:
      continue

    rank1 = cardOrder.index(card1[index])
    rank2 = cardOrder.index(card2[index])

    return 1 if rank1 < rank2 else -1

  return 0

def sortRankType(hands):
  sortedList = [] 

  for hand in hands:
    for index, sortedHand in enumerate(sortedList):
      result = compareRank(hand[0], sortedHand[0])
      if result == -1 or result == 0:
        sortedList.insert(index, hand)
        break

      if index == sortedList.__len__() - 1:
        sortedList.append(hand)
        break

    if sortedList.__len__() == 0 and hands.__len__() != 0:
      sortedList.append(hands[0])

  return sortedList

def findRank(hand):
  handSet = set(hand)
  
  if handSet.__len__() == 5:
    return "high"
  elif handSet.__len__() == 1:
    return "five"
  
  highestCount = 0
  
  for char in handSet:
    count = hand.count(char)
    if count > highestCount:
      highestCount = count

  if handSet.__len__() == 2:
    # four, full house
    return "four" if highestCount == 4 else "full"
  
  elif handSet.__len__() == 3:
    # Three, two pairs
    return "three" if highestCount == 3 else "two"

  return "one"

def main():
  totalWinning = 0
  totalWinningJoker = 0
  hands = []
  ranking = {
    "one": [],
    "two": [],
    "high": [],
    "three": [],
    "full": [],
    "four": [],
    "five": [], 
  }
  ordering = ["high", "one", "two", "three", "full", "four", "five"]

  with open ("input.txt", 'r') as file:
    for line in file.readlines():
      splitStr = line.strip().split(' ')
      rankingType = findRank(splitStr[0])
      ranking[rankingType].append((splitStr[0], int(splitStr[1])))

  rank = 1
  for type in ordering: 
    sortedList = sortRankType(ranking[type])
    for hand in sortedList:
      totalWinning += rank * hand[1]
      rank += 1

  # print(ranking)
  print(f"Part 1: The Total Winning is: {totalWinning}")
  print(f"Part 2: The Total Winning With Joker is: {totalWinningJoker}")

main()