from World import World

#Main Function
def main():
  #User input
  goalReward = raw_input('Enter the reward for the goal state: ')
  pitReward = raw_input('Enter the reward for a pit state: ')
  actionReward = raw_input('Enter the reward for taking an action: ')
  giveUpReward = raw_input('Enter the reward for giving up: ')
  trailNum = raw_input('Enter the number of trials to train the agent for: ')
  epsilon = raw_input('Enter the epsilon parameter: ')

  myWorld = World()
  myWorld.setUpWorld(goalReward, pitReward)
  myWorld.printWorld(False)




#Run the main function
if __name__ == "__main__":
    main()
