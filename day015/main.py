# Answer 1: 503487
# Answer 2: 

def main():
  file = open("input.txt", 'r')
  code = file.readlines()[0];
  sum = 0

  for line in code.split(","):
    currentValue = 0
    for char in line:
      currentValue = ((currentValue + ord(char)) * 17) % 256
    sum += currentValue
  
  print(sum)

main()