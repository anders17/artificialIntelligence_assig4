from Node import Node


#Grid World (holds all the data)
class World:
  def __init__(self,pitReward,goalReward,giveUpReward,actionReward):
      self.width = 9
      self.height = 8
      self.grid = [[Node() for j in range(0,9)] for i in range(0,8) ] #Width = 9 Height = 8
      self.pitReward = pitReward
      self.goalReward = goalReward
      self.giveUpReward = giveUpReward
      self.actionReward = actionReward

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


  #Gets the world as a string
  def getWorld(self):
    string = ""
    for i in xrange(self.height):

        for j in xrange(self.width):
          #Print the World based on the node's info
          currNode = self.grid[i][j]

          if(currNode.isWall):
            string += "X  "

          elif(currNode.isPit):
            string += "P  "

          elif(currNode.isGoal):
            string += "*  "

          else:
            string += currNode.getBestActionString() + "  "

        string += "\n"

    return string


  #Prints the node's best action reward
  def printNumsWorld(self):
      for i in xrange(self.height):
          string = ""
          for j in xrange(self.width):
              #Print the World based on the node's info
              currNode = self.grid[i][j]

              if(currNode.isWall):
                  string += "X       "

              elif(currNode.isPit):
                  string += "P       "

              elif(currNode.isGoal):
                  string += "*       "

              elif(currNode.isStart):
                  string += "S       "

              else:
                  string += str(round(currNode.possRewards[currNode.bestAction], 3)) + "  "



          print(string + "\n")

      print("-------------------------------------------------\n")

  #Prints the world
  def printWorld(self, Ai, Aj):

      for i in xrange(self.height):
          string = ""
          for j in xrange(self.width):
              #Print the World based on the node's info
              currNode = self.grid[i][j]

              if(Ai == i and Aj == j):
                  string += "A   "

              elif(currNode.isWall):
                  string += "X   "

              elif(currNode.isPit):
                  string += "P   "

              elif(currNode.isGoal):
                  string += "*   "

              elif(currNode.isStart):
                  string += "S   "

              else:
                  string += currNode.getBestActionString() + "   "

          print(string + "\n")

      print("-------------------------------------------------\n")


  # Prints recommended actions
  def printRecActions(self):
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

              elif(currNode.bestAction == 0):
                  string += "^  "

              elif (currNode.bestAction == 1):
                  string += ">  "

              elif (currNode.bestAction == 2):
                  string += "v  "

              elif (currNode.bestAction == 3):
                  string += "<  "

              elif (currNode.bestAction == -2):
                  string += "   "

              else:
                  string += "G  "

          print(string + "\n")
