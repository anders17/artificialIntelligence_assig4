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
    # outputs 1 if found pit, goal, or decided to give up; otherwise return 0
    def make_action(self,action):
        pass


    # calculate q(s,a) based on current_state and action to be taken
    # append current_state
    def updateQ(self,world,action):
        pass

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










