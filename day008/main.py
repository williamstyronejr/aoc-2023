# Answer #1: 14257
# Answer #2:

def determineMove(sequence, node, currentStep):
  side = sequence[currentStep % sequence.__len__()]
  return node[0] if side == 'L' else node[1]

def pathsFrom(startingPaths, instructions, sequence):
  steps = 0

  if startingPaths.__len__() == 1:
    currentMove = startingPaths[0]
    while currentMove != "ZZZ":
      currentMove = determineMove(sequence, instructions[currentMove], steps)
      steps += 1

  else:
    currentMoves = [x for x in startingPaths]
    endsWithZ = 0
    while endsWithZ != currentMoves.__len__():
      endsWithZ = 0

      for index, currentMove in enumerate(currentMoves):
        currentMoves[index] = determineMove(sequence, instructions[currentMove], steps)

        if currentMoves[index].endswith("Z"):
          # print("Ding!")
          endsWithZ += 1
      # print(endsWithZ)
      if endsWithZ > 2:
        print("Made it", endsWithZ, steps)
      steps += 1

  return steps

def main():
  instructions = {
    "AAA": ()
  }
  sequence = []
  stepsDefault = 0
  stepsMultiple = 0 
  startPaths = []

  with open ("input.txt", 'r') as file:
    sequence = [x for x in file.readline().strip()]
  
    for line in file.readlines():
      if not line.strip():
        continue

      str = line.split('=')
      node = str[0].strip();
      paths = str[1].replace("(", "").replace(")", "").strip().split(',')
      instructions[node] = (paths[0].strip(), paths[1].strip())

      if node.endswith("A"):
        startPaths.append(node)

  currentMove = "AAA"
  print(startPaths)

  # stepsDefault = pathsFrom(["AAA"], instructions, sequence)
  stepsMultiple = pathsFrom(startPaths, instructions, sequence)

  # while currentMove != "ZZZ":
  #   currentMove = determineMove(sequence, instructions[currentMove], steps)
  #   steps += 1

  # print(instructions)
  print(f"Part 1: Steps to reach ZZZ is: {stepsDefault}")
  print(f"Part 2: Steps for multiple paths is: {stepsMultiple}")

main()