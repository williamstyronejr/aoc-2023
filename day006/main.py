# Answer #1: 449820
# Answer #2: 42250895

def getNumOfWins(race):
  racesWon = []
  for time in range(0, race[0]):
    dist = (race[0]- time ) * time
    
    if dist > race[1]:
      racesWon.append(dist)

  return racesWon.__len__()

def main():
  raceRecord = []
  superRace = (0,0) 
  possibleWins = 1

  with open ("input.txt", 'r') as file:
    print("default")
    lines = [x.strip() for x in file.readlines()]
    times = [time for time in  lines[0].split(":")[1].strip().split(" ") if time != ""]
    distances = [distance for distance in  lines[1].split(":")[1].strip().split(" ") if distance != ""]
    superRace = (int("".join(times)), int("".join(distances)))

    for i in range(0, times.__len__()):
      raceRecord.append((int(times[i]), int(distances[i])))
  
    # Part 1
    for race in raceRecord:
      racesWon = getNumOfWins(race)
      possibleWins = possibleWins * racesWon

    # Part 2
    superRaceWins = getNumOfWins(superRace)


  print(f"Part 1: Multiple of Possible Wins {possibleWins}")
  print(f"Part 2: Possible Wins For Super Race {superRaceWins}")

main()