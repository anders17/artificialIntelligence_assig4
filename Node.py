#The class for the nodes
class Node:
    def __init__(self):
        self.isGoal = False
        self.isStart = False
        self.isPit = False
        self.isWall = False
        self.reward = -1
        #0=UP, 1=Right, 2=Down, 3= Left, 4= Give Up
        self.possRewards = [0] * 5
        self.bestAction = "^"

