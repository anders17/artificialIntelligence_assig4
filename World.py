from Node import Node

#Grid World (holds all the data)
class World:
  def __init__(self):
      self.width = 9
      self.height = 8
      self.grid = [[Node() for j in range(0,9)] for i in range(0,8) ] #Width = 9 Height = 8

  #Set up the world
  def setUpWorld(self):
      #Set rightmost and leftmost walls
      for i in xrange(self.height):
          self.grid[i][self.width-1].isWall = True
          self.grid[i][0].isWall = True

      #Set up and bottom walls
      for i in xrange(self.width):
          self.grid[self.height-1][i].isWall = True
          self.grid[0][i].isWall = True

      #Set the pits
      self.grid[3][3].isPit = True
      self.grid[3][4].isPit = True

      self.grid[4][2].isPit = True

      self.grid[5][3].isPit = True
      self.grid[5][4].isPit = True
      self.grid[5][5].isPit = True

      self.grid[4][6].isPit = True

      #set the goal
      self.grid[4][3].isGoal = True



  #Prints the world
  def printWorld(self):
      for i in xrange(self.height):
          str = ""
          for j in xrange(self.width):
              #Print the World based on the node's info
              currNode = self.grid[i][j]
              if(currNode.isWall):
                  str += "X "

              elif(currNode.isPit):
                  str += "P "

              elif(currNode.isGoal):
                  str += "G "

              elif(currNode.isStart):
                  str += "S "
              else:
                  str += "  "

          print(str + "\n")


