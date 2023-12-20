# Answer #1: 510109797
# Answer #2: 

def getCorrespondingNum(initial, ranges):
  for item in ranges:
    if initial in item[0]:
      diff = initial - item[0].start
      return item[1] + diff
    
  return initial

def getLocationNum(initial, rangeGroups):
  location = initial

  for ranges in rangeGroups:
    location = getCorrespondingNum(location, ranges)

  return location

def main():
  seedNums = []
  seedNumsFromRange = []
  ranges = []
  minSeedLocation = -1
  minSeedLocation2 = -1

  with open("input.txt", 'r') as file:
    index = 0 
    for line in file.readlines():
      if index == 0:
        seedNums += line.strip().split(":")[1].strip().split(" ")
        index += 1

        # Part 2
        for i in range(0, seedNums.__len__(), 2):

          for num in range(int(seedNums[i]), int(seedNums[i]) + int(seedNums[i+1])):
            # print(num)
            seedNumsFromRange.append(num)

      
      if line.strip() == "":
        index += 1
      elif line.__contains__(":"):
        continue
      else:
        arr = line.strip().split(" ")
        if (not index - 2 in ranges) :
          ranges.append([]) 
        start = int(arr[1])
        end = start + int(arr[2])
        maskTo = int(arr[0])

        ranges[index-2].append((range(start, end), maskTo))

  # Part 1
  for seed in seedNums:
    locationNum = getLocationNum(int(seed), ranges)

    if minSeedLocation == -1 or locationNum < minSeedLocation:
      minSeedLocation = locationNum

  # Part 2
  for seed in seedNumsFromRange:
    locationNum = getLocationNum(int(seed), ranges)

    if minSeedLocation2 == -1 or locationNum < minSeedLocation2:
      minSeedLocation2 = locationNum

  print(f"Part 1: Min Seed Location is {minSeedLocation}")
  print(f"Part 2: Min Seed Location for Range is {minSeedLocation2}")  

main()