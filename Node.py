#The class for the nodes
class Node:
    def __init__(self):
        self.isGoal = False
        self.goalReward = 0

        self.isStart = False

        self.isPit = False
        self.pitReward = 0

        self.isWall = False
        self.reward = -1
        #0=UP, 1=Right, 2=Down, 3= Left, 4= Give Up
        self.possRewards = [0] * 5
        self.bestAction = 0

    #Convert the best action index to string
    def getBestAction(self):
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


