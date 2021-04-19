"""

"""
#
# import required modules
import gym
import numpy as np
import random
#
from collections import deque
#
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
#
#
#
class deepQLearningAgent:
    """
    """
    def __init__(self, env):
        """
            deepQLearning aget initializer function
        """
        #parameters/hyperparameters definition
        # -- neural network building parameters
        self.stateSize = env.observation_space.shape[0] # take state size infofrom gym env
        self.actionSize = env.action_space.n # take action size infofrom gym env
        # --- training parameters for deep-q-learning
        self.gamma = 0.95
        self.learningRate = 0.001
        # -- epsilon-greedy parameters
        self.epsilon = 1
        self.epsilonDecay = 0.995
        self.epsilonMin = 0.01
        # -- storage parameters
        self.memory = deque(maxlen = 1000)
        # -- ANN model
        self.model = self.buildAiModel()
    #
    def buildAiModel(self):
        """
         build neural network for deepq  learning
          1 Hidden Layer
          1 Output Layer
        """
        model = Sequential()
        model.add(Dense(48, input_dim = self.stateSize, activation = "tanh")) # Hidden Layer
        model.add(Dense(self.actionSize, activation="linear")) # Output Layer 
        model.compile(loss = "mse", optimizer = Adam(lr = self.learningRate)) #calculate loss function as mse 
                                                                              # and optimizer as Adam
        return model # return builded ANN model
    #
    def remember(self, state, action, reward, nextState, done):
        """
        storage function
        """
        self.memory.append((state, action, reward, nextState, done))
    #
    def act(self, state):
        """
        acting according to state input
        """
        if random.uniform(0,1) <= self.epsilon:
            # explorarion and explotation decision
            return env.action_space.sample()
        else:
            actValues = self.model.predict(state)
            return np.argmax(actValues[0])
    #
    def replay(self, batchSize):
        """
        Training Function
        """
        if len(self.memory) < batchSize :
            return 
        else :
            miniBatch = random.sample(self.memory, batchSize)
            for state, action, reward, nextState, done in miniBatch :
                if done :
                    target = reward
                else :
                    target = reward + self.gamma*np.amax(self.model.predict(nextState)[0])
                
                trainTarget = self.model.predict(state)
                trainTarget[0][action] = target
                
                self.model.fit(state, trainTarget, verbose=0)

    #
    def adaptiveEg(self):
        """
        apply adaptive epsilon greedy approach
        """
        if self.epsilon > self.epsilonMin:
            self.epsilon = self.epsilon*self.epsilonDecay
#
#
if __name__ == "__main__":
    #
    # 1 - initialize environment and agent
    env = gym.make("CartPole-v1")
    agent = deepQLearningAgent(env)
    batchSize = 16
    episode = 100
    done = True
    for e in range(episode):
        #initialize environment
        state = env.reset()
        state = np.reshape(state, [1,4])
        time = 0
        #
        while True:
            #
            # ( step-1 ) take an action
            action = agent.act(state) #select an action
            # 
            # ( step-2 ) sexecute returned action from agent to enviranment
            nextState, reward, done, _ = env.step(action)
            nextState = np.reshape(nextState, [1,4])
            #
            # ( step-3 ) store datas
            agent.remember(state, action, reward, nextState, done)
            #
            # ( step-4 ) update states : state = nextState
            state = nextState
            #
            # ( step-5 ) Train the agent
            agent.replay(batchSize)
            #
            # ( step-6 ) adjust Epsilon, apply adaptive epsilon greedy approach
            agent.adaptiveEg()
            time = time + 1 
            if done == True:
                print("Episode : {}, Time : {}".format(e, time))
                break
#
#
# Wait user input to continue
userIn = "n"
while userIn != "y" :
    userIn = input(" press 'y' to continue visualization step : ")


# Visualize outputs
import time


trainedModel = agent
state = env.reset()
state = np.reshape(state, [1,4])

timeT = 0

while True:
    env.render()
    action = trainedModel.act(state)
    nextState, reward, done, _ = env.step(action)
    nextState = np.reshape(nextState, [1,4])
    state = nextState
    timeT += 1
    print(time)
    #time.sleep(0.4)
    if done:
        break

print("Done")