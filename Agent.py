#Agent class
import random

class Agent:
    def __init__(self, moveReward, giveUpReward):
        #Dictionary
        self.current_state = [] # example: [1,0]
        self.moveReward = moveReward
        self.giveUpReward = giveUpReward
        self.possibleMoves = 5
        self.stepSize = 0.5
        self.gama = 0.9

    # choose action
    # see if exploring
    # if not, determine move to take based on q(s,a) values
    # or give up
    def choose_action(self,world,epsilon):
        chosen_action = None
        if random.randint(0,100) < epsilon:
            pass
        else:
            pass
        return chosen_action



    # function to determine the move actually taken
    # given move desired, 10% perpendicular each direction, 10% 2x forward
    # outputs action
    def make_action(self,action):
        pass


    #Next coordinates if you take this action
    def nextCoord(self, currState, action):
        i = currState[0]
        j = currState[1]

        #Up
        if(action == 0):
          j+=1
        #Right
        elif(action == 1):
          i+=1
        #Down
        elif(action == 2):
          j-=1

        #Left
        elif(action == 3):
          i-=1

        return [i,j]



    # calculate q(s,a) based on current_state and action to be taken
    # append current_state
    def updateQ(self,world,currState, nextState, action1,action2):
        i = currState[0]
        j = currState[1]
        q1 = world.grid[i][j].possRewards[action1]


        i2 = nextState[0]
        j2 = nextState[1]
        q2 = world.grid[i2][j2].possRewards[action2]

        math = q1 + self.stepSize * (world.grid[i][j].reward + (self.gama * q2) - q1)

        #Update q1
        world.grid[i][j].possRewards[action1] = math




    def train(self,trailNum,epsilon):
        pass









