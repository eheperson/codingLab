"""
"""
import pygame
import random
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
# set window size
WIDTH = 360
HEIGHT = 360
FPS = 60
# set color codes 
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)
#
#
# define player class (inheriting from pygame.sprite )
class player(pygame.sprite.Sprite):
    #sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.radius = 10
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius )

        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 1
        self.speedX = 0
    
    def update(self, action):
        self.speedX = 0
        keyStroke = pygame.key.get_pressed()

        if keyStroke[pygame.K_LEFT] or action == 0:
            self.speedX = -4
        elif keyStroke[pygame.K_RIGHT] or action == 1:
            self.speedX = 4
        else:
            self.speedX = 0

        self.rect.x += self.speedX

        if self.rect.right > WIDTH : 
            self.rect.right = WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0
    
    def getCoordinates(self):
        return (self.rect.x, self.rect.y)
#
#
#
# define enemy class (inheriting from pygame.sprite )
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface((10,10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.radius = 5
        pygame.draw.circle(self.image, GREEN, self.rect.center, self.radius )

        self.rect.x = random.randrange(0, self.rect.width)
        self.rect.y = random.randrange(2,6)
        
        self.speedX = 0
        self.speedY = 3
    
    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if self.rect.top > HEIGHT + 10 :
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(2,6)
            self.speedY = 3

    def getCoordinates(self):
        return (self.rect.x, self.rect.y)
#
#
#
# DQL agent class
class deepQLearningAgent:
    """
    """
    def __init__(self):
        """
            deepQLearning aget initializer function
        """
        #parameters/hyperparameters definition
        # -- neural network building parameters
        self.stateSize = 4 #distances : (Xplayer-Xmob1, Yplayer-Ymob1, Xplayer-Xmob2, Yplayer-Ymob2)
        self.actionSize = 3 #right, left, noMove
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
        model.add(Dense(48, input_dim = self.stateSize, activation = "relu")) # Hidden Layer
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
        state = np.array(state)
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.actionSize)
        #
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
                state = np.array(state)
                nextState = np.array(nextState)
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
#
# environment class
class env(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #sprites
        self.allSprite = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.player = player() #player
        self.allSprite.add(self.player)
        self.mob1 = enemy() #enemy1
        self.allSprite.add(self.mob1)
        self.enemyGroup.add(self.mob1)
        self.mob2 = enemy() #enemy2
        self.allSprite.add(self.mob2)
        self.enemyGroup.add(self.mob2)
        #
        # DQL parameters
        self.reward = 0
        self.done =False
        self.totalReward = 0
        self.agent = deepQLearningAgent()
    #
    def distance(self, a, b):
        return a - b
    #
    def step(self, action):
        """
        python gym module step() function
        """
        stateList = []
        # update
        self.player.update(action)
        self.enemyGroup.update()
        # get coordinates
        #(Xplayer-Xmob1, Yplayer-Ymob1, Xplayer-Xmob2, Yplayer-Ymob2) will be our states
        nextPlayerState = self.player.getCoordinates()
        nextMob1State = self.mob1.getCoordinates()
        nextMob2State = self.mob2.getCoordinates()
        # find distances
        stateList.append(self.distance(nextPlayerState[0], nextMob1State[0]))
        stateList.append(self.distance(nextPlayerState[1], nextMob1State[1]))
        stateList.append(self.distance(nextPlayerState[0], nextMob2State[0]))
        stateList.append(self.distance(nextPlayerState[1], nextMob2State[1]))
        
        return [stateList]
    #
    def initialStates(self):
        #sprites
        self.allSprite = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.player = player() #player
        self.allSprite.add(self.player)
        self.mob1 = enemy() #enemy1
        self.allSprite.add(self.mob1)
        self.enemyGroup.add(self.mob1)
        self.mob2 = enemy() #enemy2
        self.allSprite.add(self.mob2)
        self.enemyGroup.add(self.mob2)
        #
        # DQL parameters
        self.reward = 0
        self.done =False
        self.totalReward = 0
        #
        stateList = []
        #
        # get coordinates
        PlayerState = self.player.getCoordinates()
        Mob1State = self.mob1.getCoordinates()
        Mob2State = self.mob2.getCoordinates()
        #
        # find distances
        stateList.append(self.distance(PlayerState[0], Mob1State[0]))
        stateList.append(self.distance(PlayerState[1], Mob1State[1]))
        stateList.append(self.distance(PlayerState[0], Mob1State[0]))
        stateList.append(self.distance(PlayerState[1], Mob2State[1]))
        #
        return [stateList]
    #
    def run(self):
        # game loop
        state = self.initialStates()
        running = True
        batchSize = 24
        while running:
            self.reward = 2 #define +2 point reward for each successful timestep
            #keep loop running at right speed
            clock.tick(FPS)
            #
            #process input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #
            #update game elements
            action = self.agent.act(state)
            nextState = self.step(action)
            self.totalReward += self.reward
            #
            hits = pygame.sprite.spritecollide(self.player, self.enemyGroup, False, pygame.sprite.collide_circle)
            if hits:
                self.reward = -150
                self.totalReward += self.reward
                self.done = True
                running = False
                print("Total Reward : ", self.totalReward)
            #storedatas in storage
            self.agent.remember(state, action, self.reward, nextState, self.done)
            #
            #update states
            state = nextState
            #training
            self.agent.replay(batchSize)
            #epsilon greedy approach
            self.agent.adaptiveEg()
            #draw surface
            screen.fill(GREEN)
            self.allSprite.draw(screen)
            #
            #show surface
            pygame.display.flip()
        #
        pygame.quit()
#
#
#
if __name__ == "__main__":
    env = env()
    liste = []
    t = 0
    while True:
        t += 1
        print("Episode: ",t)
        liste.append(env.totalReward)
                
        # initialize pygame and create window
        pygame.init()
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("first Game")
        clock = pygame.time.Clock()
        
        env.run()
  
