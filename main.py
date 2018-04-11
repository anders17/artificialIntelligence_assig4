from World import World
from Agent import Agent

#Main Function
def main():
  #User input
  # goalReward = input('Enter the reward for the goal state:')
  # pitReward = input('Enter the reward for a pit state:')
  # actionReward = input('Enter the reward for taking an action:')
  # giveUpReward = input('Enter the reward for giving up:')
  # trialNum = input('Enter the number of trials to train the agent for:')
  # epsilon = input('Enter the epsilon parameter:')

  #Testing Vars
  goalReward = 10
  pitReward = -200
  actionReward = -.1
  giveUpReward = -3
  trialNum = 10000

  epsilon = 0.2

  #World Setup
  myWorld = World(float(goalReward),float(pitReward),float(giveUpReward),float(actionReward))
  myWorld.setUpWorld()

  #Agent setup
  agent = Agent()
  agent.train(int(trialNum),float(epsilon),myWorld)

  print("End")


#Run the main function
if __name__ == "__main__":
    main()
