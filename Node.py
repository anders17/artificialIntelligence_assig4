#The class for the nodes
class Node:
    def __init__(self):
        self.isGoal = False

        self.isStart = False

        self.isPit = False

        self.isWall = False

        #0=UP, 1=Right, 2=Down, 3= Left
        self.possRewards = [0] * 4
        self.bestAction = 0

    #Convert the best action index to string
    def getBestActionString(self):
        action = self.bestAction

        if(action == 0):
            return "^"
        elif(action == 1):
            return ">"
        elif(action == 2):
            return "v"
        elif(action == 3):
            return "<"
        else:
            return "G"

    # Sets the bestAction
    def setBestAction(self,giveUpReward):
        chosen_action = None
        for i, reward in enumerate(self.possRewards):
            highest_q = -100000000
            if reward > highest_q:
                highest_q = reward
                chosen_action = i
        if giveUpReward > highest_q:
            chosen_action = 4
            highest_q = giveUpReward
        self.bestAction = chosen_action


