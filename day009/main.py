# Answer #1: 1798691765
# Answer #2: 1104

def getExtrapolatedVal(sequence):
  value = 0
  depth = 0

  while True:
    zeroCount = 0
    for index, num in enumerate(sequence):
      if (index == sequence.__len__() - 1 - depth):
        break

      # Storing differences in place for better performance
      sequence[index] = sequence[index+1] - num
      if sequence[index] == 0:
        zeroCount += 1
    
    if zeroCount == sequence.__len__() - depth - 1:
      value = sum(sequence[zeroCount: sequence.__len__()])
      break

    else:
      depth += 1

  return value

def main():
  sumOfValues = 0
  sumOfPreviousValues = 0

  with open ("input.txt", 'r') as file:
    for line in file.readlines():
      sequence = [int(x) for x in line.strip().split(" ")]
      reversedSequence = sequence[::-1]
      sumOfValues += getExtrapolatedVal(sequence)
      sumOfPreviousValues += getExtrapolatedVal(reversedSequence)

      

  print(f"Part 1: Sum of extrapolated values: {sumOfValues} ")
  print(f"Part 2: Sum of previous extrapolated values: {sumOfPreviousValues}")

main()