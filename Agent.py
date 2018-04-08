#Agent class
import random

class Agent:
    def __init__(self, moveReward, giveUpReward):
        #Dictionary
        self.current_state = [] # example: [1,0]
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
    # outputs action
    def make_action(self,action):
        pass


    # calculate q(s,a) based on current_state and action to be taken
    # append current_state
    def updateQ(self,world,action):
        pass










