from Node import Node

#Grid World (holds all the data)
class World:
  def __init__(self):
      self.width = 9
      self.height = 8
      self.grid = [[Node() for j in range(0,9)] for i in range(0,8) ] #Width = 9 Height = 8

  #Set up the world
  def setUpWorld(self, goalReward, pitReward):
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

      #Loop through everything and set the rewards
      for i in xrange(self.height):
          for j in xrange(self.width):
              currNode = self.grid[i][j]

              if(currNode.isPit):
                  currNode.pitReward = pitReward

              elif(currNode.isGoal):
                  currNode.goalReward = goalReward




  #Prints the world
  def printWorld(self, reward):
      for i in xrange(self.height):
          string = ""
          for j in xrange(self.width):
              #Print the World based on the node's info
              currNode = self.grid[i][j]
              if(currNode.isWall):
                  string += "X  "

              elif(currNode.isPit):
                  string += "P  "

              elif(currNode.isGoal):
                  string += "*  "

              elif(currNode.isStart):
                  string += "S  "

              elif(reward):
                  string += str(currNode.reward) + " "

              else:
                  string += currNode.getBestAction() + "  "

          print(string + "\n")


