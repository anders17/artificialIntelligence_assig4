#Agent class
import random

class Agent:
    def __init__(self):
        #Dictionary
        self.current_state = [] # example: [1,0]
        self.last_state = []

        self.last_action = -1
        self.possibleMoves = 5
        self.stepSize = 0.5
        self.gama = 0.9

    # choose action
    # see if exploring
    # if not, determine move to take based on q(s,a) values
    # or give up
    def choose_action(self, world, epsilon):
        chosen_action = None
        i = self.current_state[0]
        j = self.current_state[1]

        if random.randint(0, 100) < epsilon:
            chosen_action = random.randint(0, 3)
        else:
            highest_q = -100000000
            for i, reward in enumerate(world.grid[i][j].possRewards):
                if reward > highest_q:
                    highest_q = reward
                    chosen_action = i
            if world.giveUpReward > highest_q:
                chosen_action = 4
                highest_q = world.giveUpReward
        return chosen_action

    #returns true if it is a valid I position (based on the height of the world)
    def validI(self, i, world):
        height = world.height

        #Check if within boundaries
        if(i < height-1 and i>0):
            return True

        return False

    #returns true if it is a valid J position (based on the width of the world)
    def validJ(self, j, world):
        width = world.width

        #Check if withing boundaries and not a wall
        if(j < width-1 and j > 0):
            return True

        return False



    #returns true if this coordinate will not fall in the pit or hit a wall
    def isTerminalState(self,i,j,world):
        return (world.grid[i][j].isPit or world.grid[i][j].isGoal)

    # function to determine the move actually taken
    # given move desired, 10% perpendicular each direction, 10% 2x forward
    # outputs 1 if found pit, goal, or decided to give up; otherwise return 0
    def make_action(self, action, world):
        i = self.current_state[0]
        j = self.current_state[1]

        myRandom = random.randint(0, 9)


        #Info
        previousState = self.last_state
        currState = self.current_state
        previousAction = self.last_action
        currAction = action

        #Check if the current position is terminal state then update q and break
        if(self.isTerminalState(i,j,world) or action == 4):
            self.updateQTS(world, currState, previousState, previousAction)
            return 1


        #Normal Behavior 70%
        if(myRandom <= 6):
            # print("Normal Move")
            #Up
            if(action == 0 and self.validJ(i-1, world)):
              i-=1

            #Right
            elif(action == 1 and self.validI(j+1, world)):
              j+=1

            #Down
            elif(action == 2 and self.validJ(i+1, world)):
              i+=1

            #Left
            elif(action == 3 and self.validI(j-1, world)):
              j-=1

        #perpendicular Left 10%
        elif(myRandom == 7):
            # print("Perpendicular Left Move")
            #Up
            if(action == 0 and self.validI(j-1, world)):
              #LEFT
              j-=1

            #Right
            elif(action == 1 and self.validJ(i-1, world) ):
              #UP
              i-=1

            #Down
            elif(action == 2 and self.validI(j+1, world)):
              #RIGHT
              j+=1

            #Left
            elif(action == 3 and self.validJ(i+1, world)):
              #DOWN
              i+=1

        #Perpendicular Right 10%
        elif(myRandom == 8):
            # print("Perpendicular Right Move")
            #Up
            if(action == 0 and self.validI(j+1, world)):
              #RIGHT
              j+=1

            #Right
            elif(action == 1 and self.validJ(i+1, world)):
              #DOWN
              i+=1

            #Down
            elif(action == 2 and self.validI(j-1, world)):
              #LEFT
              j-=1

            #Left
            elif(action == 3 and self.validJ(i-1, world)):
              #UP
              i-=1



        #Double step 10%
        #NOTE: check every step
        elif(myRandom == 9):
            # print("Double Steps")
            extraSteps = 2

            for counter in xrange(extraSteps):
                #Up
                if(action == 0 and self.validJ(i-1, world)):
                  i-=1

                #Right
                elif(action == 1 and self.validI(j+1, world)):
                  j+=1

                #Down
                elif(action == 2 and self.validJ(i+1, world)):
                  i+=1

                #Left
                elif(action == 3 and self.validI(j-1, world)):
                  j-=1

                #If the new coordinates happen to be in the pit then just return them
                if(self.isTerminalState(i,j,world)):
                    #Break the loop because we have reached a terminal state
                    break

                #otherwise you can keep changing them

        #Check if this is the beginning of the walk
        if(previousAction != -1):
            self.updateQ(world, currState, previousState, previousAction, currAction)

        #update positions
        self.last_state = currState
        self.last_action = currAction
        self.current_state = [i,j]

        return 0



    #Clean agent
    def cleanAgent(self):
        self.last_action = -1
        self.last_state = []
        self.current_state = []



    # calculate q(s,a) based on current_state and action to be taken
    # append current_state
    def updateQ(self,world, currState, previousState , previousAction,currAction):
        #q1
        i = currState[0]
        j = currState[1]
        q1 = world.grid[i][j].possRewards[currAction]

        #q2
        i2 = previousState[0]
        j2 = previousState[1]
        q2 = world.grid[i2][j2].possRewards[previousAction]

        #Math to update q1 based on what we found on q2
        math = q1 + self.stepSize * (world.actionReward + (self.gama * q2) - q1)

        #Update q1
        world.grid[i2][j2].possRewards[previousAction] = math
        world.grid[i2][j2].setBestAction(world.giveUpReward)

    #Updates the previous state whenever we have reached a pit in our current position
    def updateQTS(self,world, currState, previousState, previousAction):
        #q1
        i = currState[0]
        j = currState[1]
        curNode = world.grid[i][j]

        #q2
        i2 = previousState[0]
        j2 = previousState[1]


        if(curNode.isPit):
            q1 = world.pitReward
        if(curNode.isGoal):
            q1 = world.goalReward
        else:
            q1 = world.giveUpReward
        q2 = world.grid[i2][j2].possRewards[previousAction]

        #Get the math
        math = q1 + self.stepSize * (world.actionReward + (self.gama * q2) - q1)

        #
        world.grid[i2][j2].possRewards[previousAction] = math
        world.grid[i2][j2].setBestAction(world.giveUpReward)






    #Trains the agent
    def train(self,trialNum,epsilon,world):
        for i in xrange(trialNum):
            print('Trial ' + str(i))
            iLoc = 0
            jLoc = 0
            while (world.grid[iLoc][jLoc].isPit) or (world.grid[iLoc][jLoc].isGoal) or (world.grid[iLoc][jLoc].isWall):
                iLoc = random.randint(1,world.width-2)
                jLoc = random.randint(1,world.height-2)
            self.current_state = [iLoc,jLoc]

            # Breaks when steps into a pit, the goal, or if it gives up
            while(1):
                if(i == trialNum-1):
                    currentState = self.current_state
                    world.printWorld(False, currentState[0], currentState[1])

                action = self.choose_action(world,epsilon)
                finish = self.make_action(action, world)

                Ai = self.current_state[0]
                Aj = self.current_state[1]
                world.printWorld(False,Ai, Aj)


                # if finish is true, break loop and go to next trial
                if(finish):
                    break

            self.cleanAgent()

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










