# Answer 1: 503487
# Answer 2: 261505

def calculateSumOfBox(boxes):
  """
    Calculates the sum of the ASCII values for all boxes of lens.
  """
  sum = 0

  for key in boxes.keys():
    for index, lens in enumerate(boxes[key]):
      value =  ((int(key) + 1) * (index + 1) * int(lens[1])) 
      sum = sum + value
  return sum

def runHash(sequence):
  """
    Takes in a sequence and returns the sum of all characters ASCII values.

      Parameters:
            sequence (string) String to calculate hash
      
      Returns:
            sum: (int) Sum of ASCII values for all characters in sequence
  """
  value = 0
  for char in sequence:
      value = ((value + ord(char)) * 17) % 256
    
  return value

def main():
  file = open("input.txt", 'r')
  code = file.readlines()[0];
  sum = 0
  sum2 = 0
  boxes = {}

  for sequence in code.split(","):
    # Part 1
    currentValue = runHash(sequence)
    sum += currentValue
    
    # Part 2 
    if sequence.find('=') != -1:
      replaced = False
      sections = sequence.split('=')
      label = sections[0]
      focalLen = sections[1] 
      value = runHash(label)

      if value not in boxes:
        boxes[value] = []
      
      for index, lens in enumerate(boxes[value]):
          if lens[0] == label:
            boxes[value][index][1] = focalLen
            replaced = True
            break;
      
      if not replaced:
        boxes[value].append([label, focalLen])

    elif sequence.find('-') != -1:
      sections = sequence.split('-')
      label = sections[0]
      value = runHash(label)

      # Find label in dict
      if value in boxes:
        for index, lens in enumerate(boxes[value]):
          if lens[0] == label:
            boxes[value].remove(boxes[value][index])
  
  sum2 = calculateSumOfBox(boxes)
  print(sum)
  print(sum2)

main()