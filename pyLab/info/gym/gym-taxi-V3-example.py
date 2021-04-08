import gym
env = gym.make("Taxi-v3").env

env.render() #show
# on render : 
#   blue       : passenger
#   purple     : destination
#   yellow/red : empty taxi
#   green      : full taxi
#   RGBY       : locations to take and drop
#                (destination and passenger actual location)
#
env.reset() #reset env and return random initial state
#
#
print("State Space   : ", env.observation_space) #500
print("Action Space  : ", env.action_space) #6
#
#
state = env.encode(3,1,2,2)
# env.encode(taxiRow, taxiColumn, passengerIndex, destination)
print("State Number : ", state)
#
env.s = state
env.render()
#
#
env.P[331]  #it returns : (probability, next_state, reward, done)
#
#
#
#
totalRewardList = []
for j in range(5):
    env.reset()
    timestep = 0
    totalReward = 0
    listVisualize = []
    while True:
        timestep += 1

        #choose action
        action = env.action_space.sample()

        #perform action and get reward
        nextState, reward, done, info = env.step(action) #nextState = state

        #total reward
        totalReward += reward

        #visualize
        listVisualize.append({"frame" : env,
                              "state" : state,
                              "action" : action,
                              "reward" : reward,
                              "totalReward" : totalReward})

        # env.render()
        if done:
            totalRewardList.append(totalReward)
            break

    # to visualization
    import time
    for i, frame in enumerate(listVisualize):
        print(frame["frame"].render())
        print("Timestep :", i+1)
        print("State :", frame["state"])
        print("Action :", frame["action"])
        print("Reward :", frame["reward"])
        print("Total Reward:", frame["totalReward"])
        time.sleep(2)