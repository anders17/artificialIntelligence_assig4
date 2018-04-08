#Agent class
import random

class Agent:
    def __init__(self, moveReward, giveUpReward):
        #Dictionary
        self.current_state = [] # example: [1,0]
        self.last_state = []
        self.last_action = -1
        self.moveReward = moveReward
        self.giveUpReward = giveUpReward
        self.possibleMoves = 5
        self.stepSize = 0.5
        self.gama = 0.9

    # choose action
    # see if exploring
    # if not, determine move to take based on q(s,a) values
    # or give up
    def choose_action(self, world, epsilon):
        chosen_action = None
        if random.randint(0, 100) < epsilon:
            chosen_action = random.randint(0, 5)
        else:
            highest_q = -100000000
            for i, reward in enumerate(world.grid[self.current_state[0]][self.current_state[1]].possRewards):
                if reward > highest_q:
                    highest_q = reward
                    chosen_action = i
        return chosen_action



    # function to determine the move actually taken
    # given move desired, 10% perpendicular each direction, 10% 2x forward
    # outputs 1 if found pit, goal, or decided to give up; otherwise return 0
    def make_action(self,action):
        pass


    # calculate q(s,a) based on current_state and action to be taken
    # append current_state
    def updateQ(self,world, currState, nextState, action1,action2):
        #q1
        i = currState[0]
        j = currState[1]
        q1 = world.grid[i][j].possRewards[action1]

        #q2
        i2 = nextState[0]
        j2 = nextState[1]
        q2 = world.grid[i2][j2].possRewards[action2]

        #Math to update q1 based on what we found on q2
        math = q1 + self.stepSize * (world.grid[i][j].reward + (self.gama * q2) - q1)

        #Update q1
        world.grid[i][j].possRewards[action1] = math




    def train(self,trialNum,epsilon,world):
        for i in xrange(trialNum):
            iLoc = 0
            jLoc = 0
            while (world.grid[iLoc][jLoc].isPit) or (world.grid[iLoc][jLoc].isGoal) or (world.grid[iLoc][jLoc].isWall):
                iLoc = random.randint(1,len(world.width)-2)
                jLoc = random.randint(1,len(world.height)-2)
            self.current_state = [iLoc,jLoc]

            # Breaks when steps into a pit, the goal, or if it gives up
            while(1):
                action = self.choose_action(world,epsilon)
                finish = self.make_action(action)

                # if finish is true, break loop and go to next trial
                if(finish):
                    break

        world.printRecActions()


    #Next coordinates if you take this action
    # def nextCoord(self, currState, action):
    #     i = currState[0]
    #     j = currState[1]
    #
    #     #Up
    #     if(action == 0):
    #       j+=1
    #     #Right
    #     elif(action == 1):
    #       i+=1
    #     #Down
    #     elif(action == 2):
    #       j-=1
    #
    #     #Left
    #     elif(action == 3):
    #       i-=1
    #
    #     return [i,j]










