def main():
  file = open("input.txt", 'r')
  lineCount = 0

  for line in file.readlines():
    lineCount = lineCount + 1

  print("lines ", lineCount)

main();