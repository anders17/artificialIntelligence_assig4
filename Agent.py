#Agent class
class Agent:
    def __init__(self):
        #Dictionary
        self.current_state = [] # example: [1,0]
        self.Q_pairs = {} # key is [statex,statey,action]



    # choose move
    # determine move to take based on q(s,a) values
    # update move 'state recommendation'
    def choose_move(self,world):
        pass


    # function to determine the move actually taken
    # epsilon chance random
    # given move desired, 10% perpendicular each direction, 10% 2x forward
    # outputs action
    def make_move(self,action):
        pass


    # calculate q(s,a) based on current_state and action to be taken
    # append current_state
    def updateQ(self,action,world):
        pass










