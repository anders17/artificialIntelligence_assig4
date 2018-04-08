from World import World
from Agent import Agent

#Main Function
def main():
  #User input
  goalReward = raw_input('Enter the reward for the goal state.')
  pitReward = raw_input('Enter the reward for a pit state.')
  actionReward = raw_input('Enter the reward for taking an action.')
  giveUpReward = raw_input('Enter the reward for giving up.')
  trialNum = raw_input('Enter the number of trials to train the agent for.')
  epsilon = raw_input('Enter the epsilon parameter.')

  myWorld = World()
  myWorld.setUpWorld(float(goalReward),float(pitReward))
  myWorld.printWorld(False)

  agent = Agent(float(actionReward),float(giveUpReward))
  agent.train(int(trialNum),float(epsilon))

  print("End")


#Run the main function
if __name__ == "__main__":
    main()
