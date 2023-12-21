# Answer #1: 
# Answer #2:

class Point:
  def __init__(self, x, y, direction) -> None:
    self.x = x
    self.y = y
    self.direction = direction
  
  def __str__(self) -> str:
    return f"({self.x}, {self.y}, {self.direction})"
  
  def __repr__(self) -> str:
    return f"({self.x}, {self.y}, {self.direction})"
  
  def __eq__(self, other):
    if isinstance(other, Point):
        return ((self.x == other.x) and (self.y == other.y) and (self.direction == other.direction))
    else:
        return False
      
  def __hash__(self) -> int:
    return hash(self.__repr__())

  def goLeft(self):
    self.y += -1

  def goRight(self):
    self.y += 1

  def goUp(self):
    self.x += -1

  def goDown(self):
    self.x += 1
  
  def moveOnDirection(self):
    if self.direction == 'left':
      self.goLeft()
    elif self.direction == 'right':
      self.goRight()
    elif self.direction == 'up':
      self.goUp()
    elif self.direction == 'down':
      self.goDown()

def determineMovement(pos, char):
    moves = []

    if char == '.':
      pos.moveOnDirection()
    elif char == '/':
      if pos.direction == 'left': 
        pos.direction = 'down'
      elif pos.direction == 'right':
        pos.direction = 'up'
      elif pos.direction == 'up':
        pos.direction = "right"
      else:
        pos.direction == 'left'
      
      pos.moveOnDirection()
    elif char == '\\':
      if pos.direction == 'right':
        pos.direction = 'down'
      elif pos.direction == 'down':
        pos.direction = 'right'
      elif pos.direction == 'left':
        pos.direction = 'up'
      elif pos.direction == 'down':
        pos.direction = 'left'

      pos.moveOnDirection()
    elif char == '|':
      if pos.direction == 'left' or pos.direction == 'right':
        moves.append(Point(pos.x - 1, pos.y, 'up'))
        pos.direction = 'down'

      pos.moveOnDirection()
    elif char == '-':
      if pos.direction == 'up' or pos.direction == 'down':
        moves.append(Point(pos.x, pos.y - 1, 'left'))
        pos.direction =  'right'

      pos.moveOnDirection()

    moves.append(pos)
    return moves

def startNewBeam(board, pos, visited):

    # print(pos, visited)
    print(pos)

    # Laser stops at edges of grid
    if (pos in visited) or (pos.y <= 0 and pos.direction == 'left') or (pos.y >= board[0].__len__() - 1 and pos.direction == 'right') or (pos.x <= 0 and pos.direction == 'up') or (pos.x >= board.__len__() - 1 and pos.direction == 'down'):
      return visited
    
  
    visited.add(Point(pos.x, pos.y, pos.direction))
    
    nextMoves = determineMovement(pos, board[pos.x][pos.y])
    # print (nextMoves, "\n")

    for move in nextMoves:
      startNewBeam(board, move, visited)

    return visited

def main():
    file = open("input.txt", 'r')
    input = []
    positions = [(0,0, 'right')]
    nodeVisited = set()
  
    for line in file.readlines():
          input.append([x for x in line.rstrip()])

    # Part 1
    visited =  startNewBeam(input, Point(0, 0, 'right'), nodeVisited)
    print(visited)

    print("Part #1: ", visited.__len__() ,"tiles energized ")
main()
